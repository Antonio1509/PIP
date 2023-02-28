import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox

qtCreatorFile = "Prog_09_Voto.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Bvotar.clicked.connect(self.show_dialog)


    def show_dialog(self):
        nombre = str(self.Lnombre.text())
        edad = int(self.Ledad.text())
        if edad >= 18:
            QMessageBox.about(self,"Votaciones", "Felicidades eres apto para votar " + nombre)
        else:
            QMessageBox.about(self,"Votaciones", "No eres apto para votar " + nombre)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())