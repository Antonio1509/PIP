import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_07_ImporteProducto.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.btn_agregar.clicked.connect(self.calcular)


    # Área de los Slots
    def calcular(self):

            b = int(self.txt_B.text())
            c = int(self.txt_C.text())
            r = b * c
            
            self.txt_resultado.setText(str(r))






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())