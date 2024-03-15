from PyQt5 import QtWidgets

from mywindow import mywindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())
