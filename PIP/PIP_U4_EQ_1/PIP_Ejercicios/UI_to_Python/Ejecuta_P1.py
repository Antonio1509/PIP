import sys

from PyQt5 import uic, QtWidgets

from PIP_U4_EQ_1.PIP_Ejercicios.UI_to_Python import P1_Ejemplo as interfaz


class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_fahr.clicked.connect(self.conversion)

    # Área de los slots
    def conversion(self):
        cent = int(self.txt_cent.text())
        fahr = cent * 1.8 + 32
        self.txt_fahr.setText(str(fahr))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())