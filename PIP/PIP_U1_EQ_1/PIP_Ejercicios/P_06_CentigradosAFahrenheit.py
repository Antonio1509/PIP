import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_06_CentigradosAFahrenheit.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_conversion.clicked.connect(self.conversion)

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