# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1205, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(271, 391))
        self.tabWidget.setMaximumSize(QtCore.QSize(271, 391))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.faaenable = QtWidgets.QRadioButton(self.tab)
        self.faaenable.setGeometry(QtCore.QRect(10, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.faaenable.setFont(font)
        self.faaenable.setObjectName("faaenable")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 80, 223, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.faafpline = QtWidgets.QLineEdit(self.widget)
        self.faafpline.setObjectName("faafpline")
        self.faafpline.setText("35")
        self.horizontalLayout_6.addWidget(self.faafpline)
        self.faafpbox = QtWidgets.QComboBox(self.widget)
        self.faafpbox.setObjectName("faafpbox")
        self.faafpbox.addItem("")
        self.faafpbox.addItem("")
        self.faafpbox.setCurrentIndex(1)
        self.horizontalLayout_6.addWidget(self.faafpbox)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(10, 120, 222, 26))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.faafaline = QtWidgets.QLineEdit(self.widget1)
        self.faafaline.setObjectName("faafaline")
        self.faafaline.setText("70")
        self.horizontalLayout_7.addWidget(self.faafaline)
        self.faafabox = QtWidgets.QComboBox(self.widget1)
        self.faafabox.setObjectName("faafabox")
        self.faafabox.addItem("")
        self.faafabox.addItem("")
        self.faafabox.setCurrentIndex(1)
        self.horizontalLayout_7.addWidget(self.faafabox)
        self.widget2 = QtWidgets.QWidget(self.tab)
        self.widget2.setGeometry(QtCore.QRect(10, 160, 167, 26))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.faaapline = QtWidgets.QLineEdit(self.widget2)
        self.faaapline.setObjectName("faaapline")
        self.faaapline.setText("1")
        self.horizontalLayout_8.addWidget(self.faaapline)
        self.widget3 = QtWidgets.QWidget(self.tab)
        self.widget3.setGeometry(QtCore.QRect(10, 200, 166, 26))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.faaaaline = QtWidgets.QLineEdit(self.widget3)
        self.faaaaline.setObjectName("faaaaline")
        self.faaaaline.setText("48")
        self.horizontalLayout_9.addWidget(self.faaaaline)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.shenabale = QtWidgets.QRadioButton(self.tab_2)
        self.shenabale.setGeometry(QtCore.QRect(10, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.shenabale.setFont(font)
        self.shenabale.setObjectName("shenabale")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 90, 223, 26))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.shfrecline = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.shfrecline.setObjectName("shfrecline")
        self.shfrecline.setText("140")
        self.horizontalLayout_10.addWidget(self.shfrecline)
        self.shfrecbox = QtWidgets.QComboBox(self.layoutWidget_2)
        self.shfrecbox.setObjectName("shfrecbox")
        self.shfrecbox.addItem("")
        self.shfrecbox.addItem("")
        self.shfrecbox.setCurrentIndex(1)
        self.horizontalLayout_10.addWidget(self.shfrecbox)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.llaveanalenable = QtWidgets.QRadioButton(self.tab_3)
        self.llaveanalenable.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.llaveanalenable.setFont(font)
        self.llaveanalenable.setObjectName("llaveanalenable")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.frenable = QtWidgets.QRadioButton(self.tab_4)
        self.frenable.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.frenable.setFont(font)
        self.frenable.setObjectName("frenable")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 90, 223, 26))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.frfpline = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.frfpline.setObjectName("frfpline")
        self.frfpline.setText("35")
        self.horizontalLayout_11.addWidget(self.frfpline)
        self.frfpbox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.frfpbox.setObjectName("frfpbox")
        self.frfpbox.addItem("")
        self.frfpbox.addItem("")
        self.frfpbox.setCurrentIndex(1)
        self.horizontalLayout_11.addWidget(self.frfpbox)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 130, 222, 26))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.frfaline = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.frfaline.setObjectName("frfaline")
        self.frfaline.setText("70")
        self.horizontalLayout_12.addWidget(self.frfaline)
        self.frfabox = QtWidgets.QComboBox(self.layoutWidget_4)
        self.frfabox.setObjectName("frfabox")
        self.frfabox.addItem("")
        self.frfabox.addItem("")
        self.frfabox.setCurrentIndex(1)
        self.horizontalLayout_12.addWidget(self.frfabox)
        self.layoutWidget_5 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 190, 167, 26))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.frapline = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.frapline.setObjectName("frapline")
        self.frapline.setText("1")
        self.horizontalLayout_13.addWidget(self.frapline)
        self.layoutWidget_6 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 240, 166, 26))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.fraaline = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.fraaline.setObjectName("fraaline")
        self.fraaline.setText("48")
        self.horizontalLayout_14.addWidget(self.fraaline)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(901, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(3)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4.addWidget(self.frame)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(271, 291))
        self.frame_3.setMaximumSize(QtCore.QSize(271, 291))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.xinbox = QtWidgets.QComboBox(self.frame_3)
        self.xinbox.setGeometry(QtCore.QRect(10, 80, 91, 22))
        self.xinbox.setAutoFillBackground(False)
        self.xinbox.setDuplicatesEnabled(False)
        self.xinbox.setFrame(True)
        self.xinbox.setObjectName("xinbox")
        self.xinbox.addItem("")
        self.xinbox.addItem("")
        self.xinbox.setCurrentIndex(1)
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 170, 231, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.xinampline = QtWidgets.QLineEdit(self.layoutWidget)
        self.xinampline.setObjectName("xinampline")
        self.xinampline.setText("1")
        self.horizontalLayout_2.addWidget(self.xinampline)
        self.xinampbox = QtWidgets.QComboBox(self.layoutWidget)
        self.xinampbox.setObjectName("xinampbox")
        self.xinampbox.addItem("")
        self.xinampbox.addItem("")
        self.horizontalLayout_2.addWidget(self.xinampbox)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 220, 131, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.xindutyline = QtWidgets.QLineEdit(self.layoutWidget1)
        self.xindutyline.setObjectName("xindutyline")
        self.xindutyline.setText("0.75")
        self.horizontalLayout_3.addWidget(self.xindutyline)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 120, 231, 26))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.xinfrecline = QtWidgets.QLineEdit(self.layoutWidget2)
        self.xinfrecline.setObjectName("xinfrecline")
        self.xinfrecline.setText("7.5")
        self.horizontalLayout.addWidget(self.xinfrecline)
        self.xinfrecbox = QtWidgets.QComboBox(self.layoutWidget2)
        self.xinfrecbox.setObjectName("xinfrecbox")
        self.xinfrecbox.addItem("")
        self.xinfrecbox.addItem("")
        self.xinfrecbox.setCurrentIndex(1)
        self.horizontalLayout.addWidget(self.xinfrecbox)
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(901, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.faaenable.setText(_translate("MainWindow", "Enable"))
        self.label_5.setText(_translate("MainWindow", "Fp"))
        self.faafpbox.setItemText(0, _translate("MainWindow", "Hz"))
        self.faafpbox.setItemText(1, _translate("MainWindow", "KHz"))
        self.label_6.setText(_translate("MainWindow", "Fa"))
        self.faafabox.setItemText(0, _translate("MainWindow", "Hz"))
        self.faafabox.setItemText(1, _translate("MainWindow", "KHz"))
        self.label_8.setText(_translate("MainWindow", "Ap"))
        self.label_7.setText(_translate("MainWindow", "Aa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "FAA"))
        self.shenabale.setText(_translate("MainWindow", "Enable"))
        self.label_9.setText(_translate("MainWindow", "Frecuencia"))
        self.shfrecbox.setItemText(0, _translate("MainWindow", "Hz"))
        self.shfrecbox.setItemText(1, _translate("MainWindow", "KHz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "S/H"))
        self.llaveanalenable.setText(_translate("MainWindow", "Enable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "LLave Analógica"))
        self.frenable.setText(_translate("MainWindow", "Enable"))
        self.label_10.setText(_translate("MainWindow", "Fp"))
        self.frfpbox.setItemText(0, _translate("MainWindow", "Hz"))
        self.frfpbox.setItemText(1, _translate("MainWindow", "KHz"))
        self.label_11.setText(_translate("MainWindow", "Fa"))
        self.frfabox.setItemText(0, _translate("MainWindow", "Hz"))
        self.frfabox.setItemText(1, _translate("MainWindow", "KHz"))
        self.label_12.setText(_translate("MainWindow", "Ap"))
        self.label_13.setText(_translate("MainWindow", "Aa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "FR"))
        self.label.setText(_translate("MainWindow", "Señal de Entrada"))
        self.xinbox.setItemText(0, _translate("MainWindow", "Senoidal"))
        self.xinbox.setItemText(1, _translate("MainWindow", "Cuadrada"))
        self.label_3.setText(_translate("MainWindow", "Amplitud:"))
        self.xinampbox.setItemText(0, _translate("MainWindow", "V"))
        self.xinampbox.setItemText(1, _translate("MainWindow", "mV"))
        self.label_4.setText(_translate("MainWindow", "Duty:"))
        self.label_2.setText(_translate("MainWindow", "Frecuencia:"))
        self.xinfrecbox.setItemText(0, _translate("MainWindow", "Hz"))
        self.xinfrecbox.setItemText(1, _translate("MainWindow", "KHz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
