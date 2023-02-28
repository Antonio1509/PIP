import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_08_SumaDosNumeros.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.slider_a.setMinimum(-100)
        self.slider_a.setMaximum(100)
        self.slider_a.setSingleStep(1)
        self.slider_a.setValue(0)

        self.slider_b.setMinimum(-100)
        self.slider_b.setMaximum(100)
        self.slider_b.setSingleStep(1)
        self.slider_b.setValue(0)

        self.slider_a.valueChanged.connect(self.cambiaValorA)
        self.slider_b.valueChanged.connect(self.cambiaValorB)

        self.txt_valorA.setText("0")
        self.txt_valorB.setText("0")

    # Área de los slots
    def cambiaValorA(self):
        self.txt_valorA.setText(str(self.slider_a.value()))
        self.realizarSuma()

    def cambiaValorB(self):
        self.txt_valorB.setText(str(self.slider_b.value()))
        self.realizarSuma()

    def realizarSuma(self):
        a = self.slider_a.value()
        b = self.slider_b.value()
        self.txt_resultado.setText(str(a+b))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())