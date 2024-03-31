from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from interfaz import Ui_MainWindow
import pyqtgraph as pg
import snh
import copy
import numpy as np

class mywindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.sim = snh.Sim(10e-3, 1e-7)
        # Connect everything
        self.sim.makeCircuit({
            'wave': self.sim.gen_square_wave(7.5e3, 1, 0.75),
            'filter': snh.Chevy1_LPF(fp=35e3, fa=2*35e3, Ap=1, Aa=40),
            'zoh': snh.ZOH(f_sample=1e5, sim=self.sim),
            'switch': snh.Switch(f_sample=1e5, sim=self.sim),
            'recovery_filter': snh.Chevy1_LPF(fp=35e3, fa=2*35e3, Ap=1, Aa=40),
        })

        self.setupUi(self)
        self.connectEvents()
        self.initplots()
        self.update_plots()
        
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
    def getEnable(self, key):
        l=["faa","sh","switch","fr"]
        v = [
            self.faaenable.isChecked(),
            self.shenabale.isChecked(),
            self.llaveanalenable.isChecked(),
            self.frenable.isChecked()
        ]
        return dict(zip(l,v))[key]
    
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
        l=["fp","fp_mult","fa","fa_mult","ap","aa"]
        v=[
            self.getNum(self.faafpline),            # fp
            self.getMultiplier(self.faafpbox,0),    # fp_mult
            self.getNum(self.faafaline),            # fa
            self.getMultiplier(self.faafabox,0),    # fa_mult
            self.getNum(self.faaapline),            # ap
            self.getNum(self.faaaaline)             # aa
        ]
        return dict(zip(l,v))
        
    #retunea los parametros del SH
    def getSh(self):
        l=["f","f_mult"]
        v=[
            self.getNum(self.shfrecline),
            self.getMultiplier(self.shfrecbox,0)
        ]
        return dict(zip(l,v))
    
    #retunea los parametros del FR
    def getFr(self):
        l=["fp","fp_mult","fa","fa_mult","ap","aa"]
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
        # Tab Changed
        self.tabWidget.currentChanged.connect(lambda: print(self.getTabIndex()))

        # Input Signal
        self.xinbox.activated.connect(lambda: self.setWave())  # ID Señal de entrada
        self.xinfrecline.textChanged.connect(lambda: self.setWave())
        self.xinfrecbox.activated.connect(lambda: self.setWave())
        self.xinampline.textChanged.connect(lambda: self.setWave())
        self.xinampbox.activated.connect(lambda: self.setWave())
        self.xindutyline.textChanged.connect(lambda: self.setWave())

        # FAA
        self.faafpline.textChanged.connect(lambda: self.setFAA())
        self.faafpbox.activated.connect(lambda: self.setFAA())
        self.faafaline.textChanged.connect(lambda: self.setFAA())
        self.faafabox.activated.connect(lambda: self.setFAA())
        self.faaapline.textChanged.connect(lambda: self.setFAA())
        self.faaaaline.textChanged.connect(lambda: self.setFAA())        
        self.faaenable.toggled.connect(lambda: self.setFAA())

        # Sample and Hold
        self.shenabale.toggled.connect(lambda: self.setSampleAndHold())
        self.shfrecbox.activated.connect(lambda: self.setSampleAndHold())
        self.shfrecline.textChanged.connect(lambda: self.setSampleAndHold())

        # Switch
        self.llaveanalenable.toggled.connect(lambda: self.setSampleAndHold())   # Uso  la misma funcion

        # Recovery Filter
        self.frenable.toggled.connect(lambda: self.setRecoveryFilter())
        self.frfpline.textChanged.connect(lambda: self.setRecoveryFilter())
        self.frfpbox.activated.connect(lambda: self.setRecoveryFilter())
        self.frfaline.textChanged.connect(lambda: self.setRecoveryFilter())
        self.frfabox.activated.connect(lambda: self.setRecoveryFilter())
        self.frapline.textChanged.connect(lambda: self.setRecoveryFilter())
        self.fraaline.textChanged.connect(lambda: self.setRecoveryFilter())

        
    #inicializa los plots
    def initplots(self):
        #creo horizontal layouts
        self.horizontalLayout_15 = QtWidgets.QVBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_18")
        self.horizontalLayout_16 = QtWidgets.QVBoxLayout(self.frame_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_19")
        
        #Creo a PyQtGraph PlotWidget
        self.plot_widget_1 = pg.PlotWidget()
        self.plot_widget_1.setLabel('left', 'Amplitud', units='V')
        self.plot_widget_1.setLabel('bottom', 'Tiempo', units='s')
        self.plot_widget_1.plotItem.showGrid(True, True)
        
        self.plot_widget_2 = pg.PlotWidget()
        self.plot_widget_2.setLabel('left', 'Amplitud', units='V')
        self.plot_widget_2.setLabel('bottom', 'Frecuencia', units='Hz')
        self.plot_widget_2.plotItem.setLogMode(True, False)
        self.plot_widget_2.plotItem.showGrid(True, True)
        
        #Lo agrego a los layouts
        self.horizontalLayout_15.addWidget(self.plot_widget_1)
        self.horizontalLayout_16.addWidget(self.plot_widget_2)
             






    def update_plots(self):
        # Get the traces
        traces = self.sim.simulate()        # TODO: Implementar mostrar el grafico del tab actual
        output = self.sim.output

        # Update the plots
        self.plot_widget_1.clear()
        self.plot_widget_2.clear()

        self.plot_widget_1.plot(self.sim.time_array, output, pen='r')

        n = len(output)
        X = np.fft.rfft(output)
        X = X / n
        freqs = np.fft.rfftfreq(n, d=self.sim.dt)
        print( len(X), len(freqs) )
        self.plot_widget_2.plot(freqs, np.abs(X), pen='r')
        

    def setWave(self):
        # ["tipo","f","f_mult", "amp", "amp_mult","duty"]
        xinDict = self.getXin()
        frec = xinDict["f"] * xinDict["f_mult"]
        amp = xinDict["amp"] * xinDict["amp_mult"]
        duty = xinDict["duty"]

        #0 senoidal, 1 cuadrada, 2 triangular
        if xinDict["tipo"] == 0:
            self.sim.components["wave"] = self.sim.gen_sine_wave(frec, amp)
        elif xinDict["tipo"] == 1:
            self.sim.components["wave"] = self.sim.gen_square_wave(frec, amp, duty)

        self.update_plots()

    def setFAA(self):
        faaDict = self.getFaa()
        fp = faaDict["fp"] * faaDict["fp_mult"]
        fa = faaDict["fa"] * faaDict["fa_mult"]
        self.sim.components["filter"].redesign(fp, fa, faaDict["ap"], faaDict["aa"])
        self.sim.components["filter"].enabled = self.getEnable("faa")
        
        # fil = self.sim.components["filter"]
        # fil.print_debug()
        self.update_plots()

    def setSampleAndHold(self):
        shDict = self.getSh()
        f_sample = shDict["f"] * shDict["f_mult"]
        if not isinstance(f_sample, float) or f_sample == 0:
            QMessageBox.warning(self, "Error", "Frecuencia de muestreo no puede ser 0")
            return
        self.sim.components["zoh"].setup(f_sample=f_sample, sim=self.sim)
        self.sim.components["zoh"].enabled = self.getEnable("sh")
        self.sim.components["switch"].enabled = self.getEnable("switch")
        self.update_plots()        

    def setRecoveryFilter(self):
        frDict = self.getFr()
        fp = frDict["fp"] * frDict["fp_mult"]
        fa = frDict["fa"] * frDict["fa_mult"]
        self.sim.components["recovery_filter"].redesign(fp, fa, frDict["ap"], frDict["aa"])
        self.sim.components["recovery_filter"].enabled = self.getEnable("fr")
        self.update_plots()