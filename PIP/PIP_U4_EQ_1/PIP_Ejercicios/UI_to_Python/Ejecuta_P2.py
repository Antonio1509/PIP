import sys

from PyQt5 import uic, QtWidgets

from PIP_U4_EQ_1.PIP_Ejercicios.UI_to_Python import P2_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_exp.clicked.connect(self.calcular)

    # Área de los slots
    def calcular(self):
        try:
            expresion = self.txt_exp.text()
            result = eval(expresion)
            print(result)
            self.txt_prom.setText(str(result))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())