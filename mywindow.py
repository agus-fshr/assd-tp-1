from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from interfaz import Ui_MainWindow
import pyqtgraph as pg
import snh
import copy

class mywindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.sim = snh.Sim(1e-3, 1e-9)
        # Connect everything
        self.sim.makeCircuit({
            'square_wave': self.sim.gen_square_wave(7.5e3, 1, 0.75),
            'filter': snh.Chevy1_LPF(fp=35e3, fa=2*35e3, Ap=1, Aa=40),
            'zoh': snh.ZOH(f_sample=1e5, sim=self.sim),
            'switch': snh.Switch(f_sample=1e5, sim=self.sim),
            'recovery_filter': snh.Chevy1_LPF(fp=35e3, fa=2*35e3, Ap=1, Aa=40),
        })

        self.setupUi(self)
        self.connectEvents()
        self.initplots()
        
    #extrae el número ingresado
    def getNum(self, lineedit):
        try:
            return float((lineedit.text()).replace(',','.'))
        except:
            return 0
            
    #extrae indice
    def getIndex(self, combobox):
        return combobox.currentIndex()
    
    #returns multiplier
    def getMultiplier(self, combobox, flag):
        comboboxindex = combobox.currentIndex()
        if flag == 0:               #si el flag es 0 entonces es frecuencia
            if comboboxindex == 0:      # Hz
                multiplier = 1
            elif comboboxindex == 1:    # KHz
                multiplier = 1000
        else:
            if comboboxindex == 0:      # V
                multiplier = 1
            elif comboboxindex == 1:    # mV
                multiplier = 0.001
        return multiplier

    #devuelve el tab en el cual estas
    def getTabIndex(self):
        return self.tabWidget.currentIndex()
    
    #retunea que esta prendido
    def getEnable(self):
        l=["Faa","SH","llaveAnal","Fr"]
        v = [
            self.faaenable.isChecked(),
            self.shenabale.isChecked(),
            self.llaveanalenable.isChecked(),
            self.frenable.isChecked()
        ]
        return dict(zip(l,v))
    
    #returnea los parametros de entrada
    def getXin(self):
        l=["tipo","f","f_mult", "amp", "amp_mult","duty"]
        v=[
            self.getIndex(self.xinbox),             #0 senoidal, 1 cuadrada, 2 triangular
            self.getNum(self.xinfrecline),
            self.getMultiplier(self.xinfrecbox,0),
            self.getNum(self.xinampline),
            self.getMultiplier(self.xinampbox,1),
            self.getNum(self.xindutyline)
        ]
        print(self.getIndex(self.xinbox), self.xinbox)
        return dict(zip(l,v))
        
    #retunea los parametros del FAA
    def getFaa(self):
        l=["fp","fp multi","fa","fa multi","Ap","Aa"]
        v=[
            self.getNum(self.faafpline),
            self.getMultiplier(self.faafpbox,0),
            self.getNum(self.faaaline),
            self.getMultiplier(self.faaabox,0),
            self.getNum(self.faaapline),
            self.getNum(self.faaaaline)
        ]
        return dict(zip(l,v))
        
    #retunea los parametros del SH
    def getSh(self):
        l=["frec","frec multi"]
        v=[
            self.getNum(self.shfrecline),
            self.getMultiplier(self.shfrecbox,0)
        ]
        return dict(zip(l,v))
    
    #retunea los parametros del FR
    def getFr(self):
        l=["fp","fp multi","fa","fa multi","Ap","Aa"]
        v=[
            self.getNum(self.frfpline),
            self.getMultiplier(self.frfpbox,0),
            self.getNum(self.frfaline),
            self.getMultiplier(self.frfabox,0),
            self.getNum(self.frapline),
            self.getNum(self.fraaline)
        ]
        return dict(zip(l,v))
    
    def connectEvents(self):
        # Input Signal
        self.tabWidget.currentChanged.connect(lambda: print(self.getTabIndex()))
        self.xinbox.activated.connect(lambda: self.setWave())  # ID Señal de entrada
        self.xinfrecline.textChanged.connect(lambda: self.setWave())
        self.xinfrecbox.activated.connect(lambda: self.setWave())
        self.xinampline.textChanged.connect(lambda: self.setWave())
        self.xinampbox.activated.connect(lambda: self.setWave())
        self.xindutyline.textChanged.connect(lambda: self.setWave())

        # FAA
        self.faafpline.textChanged.connect(lambda: print("fp"))
        self.faafpbox.activated.connect(lambda: print("fpbox"))
        self.faafaline.textChanged.connect(lambda: print("fa"))
        self.faafabox.activated.connect(lambda: print("fabox"))
        self.faaapline.textChanged.connect(lambda: print("ap"))
        self.faaaaline.textChanged.connect(lambda: print("aa"))        

        # Sample and Hold
        self.shenabale.toggled.connect(lambda: self.setSampleAndHold())
        
    #inicializa los plots
    def initplots(self):
        #creo horizontal layouts
        self.horizontalLayout_15 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_18")
        self.horizontalLayout_16 = QtWidgets.QVBoxLayout(self.frame_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_19")
        
        #Creo a PyQtGraph PlotWidget
        self.plot_widget_1 = pg.PlotWidget()
        self.plot_widget_2 = pg.PlotWidget()
        
        #Lo agrego a los layouts
        self.horizontalLayout_15.addWidget(self.plot_widget_1)
        self.horizontalLayout_16.addWidget(self.plot_widget_2)
             
    def update_plots(self):

    def setWave(self):
        # ["tipo","f","f_mult", "amp", "amp_mult","duty"]
        xinDict = self.getXin()
        frec = xinDict["f"] * xinDict["f_mult"]
        amp = xinDict["amp"] * xinDict["amp_mult"]
        duty = xinDict["duty"]

        if xinDict["tipo"] == 1: #0 senoidal, 1 cuadrada, 2 triangular
            self.sim.components["wave"] = self.sim.gen_square_wave(frec, amp, duty)

    def setSampleAndHold(self):
        shDict = self.getSh()
        isChecked = self.shenabale.isChecked()
        print(shDict, isChecked)