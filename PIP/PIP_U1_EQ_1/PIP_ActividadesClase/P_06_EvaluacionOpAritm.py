import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_06_EvaluacionOpAritm.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
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