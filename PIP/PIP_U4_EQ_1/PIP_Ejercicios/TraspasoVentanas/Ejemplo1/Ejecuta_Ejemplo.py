import sys
from PyQt5 import uic, QtWidgets

###########################################################################################
from PIP_U4_EQ_1.PIP_Ejercicios.TraspasoVentanas.Ejemplo1 import EnviaInfoMain as main, EnviaInfoDialog as second
class MyMainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        main.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        ## Área de los Signals
        self.btn_saludar.clicked.connect(self.saludar)

    # Área de los slots
    def saludar(self):
        n = self.txt_nombre.text()
        self.dialogo = second.MyDialog()
        self.dialogo.setModal(True)
        self.dialogo.txt_nombre.setText(str(n))
        self.dialogo.show()

###########################################################################################
'''from PIP_U4_EQ_1.PIP_Ejercicios.TraspasoVentanas.Ejemplo1 import EnviaInfoDialog as second
class MyDialog(QtWidgets.QDialog, second.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        second.Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals

    # Área de los slots
'''
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
