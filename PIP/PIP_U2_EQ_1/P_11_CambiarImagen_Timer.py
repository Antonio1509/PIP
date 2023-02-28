import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "Prog_11_CambiaImagen_Timer.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.slider_imagenes)

        self.slider_img.setMinimum(0)
        self.slider_img.setMaximum(5)
        self.slider_img.setSingleStep(0)
        self.slider_img.setValue(0)

        self.slider_img.valueChanged.connect(self.cambiaImagen)

        self.listaImgs = []
        self.listaImgs.append(["Numero 1", ":/AutosF1/redbull.png"])
        self.listaImgs.append(["Numero 2", ":/AutosF1/mercedes.jpg"])
        self.listaImgs.append(["Numero 3", ":/AutosF1/ferrari.jpg"])
        self.listaImgs.append(["Numero 4", ":/AutosF1/alpine.jpg"])
        self.listaImgs.append(["Numero 5", ":/AutosF1/mclaren.jpg"])
        self.listaImgs.append(["Numero 6", ":/AutosF1/haas.jpg"])

        self.txt_valorA.setText("Numero 1")

        self.IndexImagen = 0

        self.segundoPlano.start(250)

    # Área de los slots
    def slider_imagenes(self):
        self.slider_img.setValue(self.IndexImagen)
        self.IndexImagen = (self.IndexImagen+1)%6

    def cambiaImagen(self):
        try:
            imagen = self.listaImgs[self.slider_img.value()]
            self.txt_valorA.setText(imagen[0])
            self.img.setPixmap(QtGui.QPixmap(imagen[1]))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())