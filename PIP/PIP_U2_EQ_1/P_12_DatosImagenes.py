import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "Prog_12_DatosImagenes.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
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

        import Modulo_Contactos as contactos
        self.contacts = contactos.cargarContactos()
        self.obtieneDatosContacto[0]

    # Área de los slots
    def cambiaImagen(self):
        indice = self.slider_img.value()
        imagen = self.listaImgs[self.slider_img.value()]
        self.txt_valorA.setText(imagen[0])
        self.img.setPixmap(QtGui.QPixmap(imagen[1]))
        self.obtieneDatosContacto(indice)

    def obtieneDatosContacto(self, indice):
        datosContacto = self.contacts[indice]
        self.txt_equipo.setText(datosContacto[0])
        self.txt_piloto.setText(datosContacto[1])
        self.txt_numero.setText(datosContacto[2])
        self.txt_year.setText(datosContacto[3])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())