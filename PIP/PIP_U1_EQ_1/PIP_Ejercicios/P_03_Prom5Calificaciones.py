import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_03_Prom5Calificaciones.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_calcular.clicked.connect(self.calcular)

        self.calificaciones = []  #lista vacia

    # Área de los Slots

    def calcular(self):
            a = int(self.txt_A.text())
            b = int(self.txt_B.text())
            c = int(self.txt_C.text())
            d = int(self.txt_D.text())
            e = int(self.txt_E.text())
            r = a + b + c + d + e
            p = r/5
            self.txt_resultado.setText(str(p))




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())