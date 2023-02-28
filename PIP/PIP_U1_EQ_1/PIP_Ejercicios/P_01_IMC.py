import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_01_IMC.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Bcalcular.clicked.connect(self.Calcular)

    def Calcular(self):
        altura = float(self.Laltura.text())
        peso = int(self.Lpeso.text())
        datos = peso/(altura**2)

        self.Limc.setText(str(datos))


if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())