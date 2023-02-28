import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_02_DistanciaentreDosPuntos.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_distancia.clicked.connect(self.distancia)

    # Área de los slots
    def distancia(self):
        a = int(self.txt_A.text())
        b = int(self.txt_B.text())
        r = a+b
        self.txt_resultado.setText(str(r))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())