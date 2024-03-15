from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from interfaz import Ui_MainWindow

class mywindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        
    #extrae el número ingresado
    def getnum(self, lineedit):
        try:
            return float((lineedit.text()).replace(',','.'))
        except:
            return 0
            
    #extrae indice
    def getindex(self, combobox):
        return combobox.currentIndex()
    
    #returns multiplier
    def get_multiplier(self, combobox):
        comboboxindex = combobox.currentIndex()
        if comboboxindex == 0:
            multiplier = 1
        elif comboboxindex == 1:
            multiplier = 1000
        return multiplier
    
    