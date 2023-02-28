import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "Prog_10_unidades.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


        self.btn_cen.clicked.connect(self.centenas)
        self.btn_dec.clicked.connect(self.decenas)
        self.btn_uni.clicked.connect(self.unidades)


    def centenas (self):
        num = int(self.Lnumero.text())
        c = num / 100
        self.txt_centenas.setText(str(c) + "-" + "centenas")

    def decenas (self):
        num = int(self.Lnumero.text())
        d = num / 10
        self.txt_decenas.setText(str(d) + "-" + "decenas")



    def unidades (self):
        num = int(self.Lnumero.text())
        self.txt_unidades.setText(str(num) + "-" + "unidades")


    def mensaje (self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exect_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())