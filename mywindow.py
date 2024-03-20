from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from interfaz import Ui_MainWindow
import pyqtgraph as pg

class mywindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.update()
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
            if comboboxindex == 0:
                multiplier = 1
            elif comboboxindex == 1:
                multiplier = 1000
        else:
            if comboboxindex == 0:
                multiplier = 1
            elif comboboxindex == 1:
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
        l=["tipo","frec","frec multi", "amplitud", "amplitud multi","duty"]
        v=[
            self.getIndex(self.xinbox),             #0 senoidal, 1 cuadrada, 2 triangular
            self.getNum(self.xinfrecline),
            self.getMultiplier(self.xinfrecbox,0),
            self.getNum(self.xinampline),
            self.getMultiplier(self.xinampbox,1),
            self.getNum(self.xindutyline)
        ]
        return dict(zip(l,v))
        
    def update(self):
        self.tabWidget.currentChanged.connect(lambda: print(self.getTabIndex()))
        self.xinbox.activated.connect(lambda: print("xinbox"))
        self.xinfrecline.textChanged.connect(lambda: print("frecline"))
        self.xinfrecbox.activated.connect(lambda: print("frecbox"))
        self.xinampline.textChanged.connect(lambda: print("ampline"))
        self.xinampbox.activated.connect(lambda: print("ampbox"))
        self.xindutyline.textChanged.connect(lambda: print("dutyline"))
        
        
        
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
             
        