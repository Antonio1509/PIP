import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_08_CalculodeVelocidad.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_vel.clicked.connect(self.vel)

    # Área de los slots
    def vel(self):
        a = int(self.txt_dis.text())
        b = int(self.txt_time.text())
        res = a / b
        self.txt_resultado.setText(str(res))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())