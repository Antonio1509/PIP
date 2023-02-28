import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_05_KilometrosAMetros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_leer.clicked.connect(self.sumar)

    # Área de los Slots
    def sumar(self):
        a = int(self.txt_A.text())
        r = a*1000
        self.txt_resulta.setText(str(r)+"-"+"metros")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())