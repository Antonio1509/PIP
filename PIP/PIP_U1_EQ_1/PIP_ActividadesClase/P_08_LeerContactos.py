import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_08_LeerContactos.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_read.clicked.connect(self.leercontactos)

    # Área de los slots
    def leercontactos(self):
        info_contactos = self.leerArchivo()
        contactos = []
        for linea in info_contactos:
            linea = linea.replace("\n","")
            c = linea.split(",")
            contactos.append(c)
        print(contactos)

        texto = ""
        for con in contactos:
            texto += str(con) + "\n"
        self.txt_vista.setText(texto)

    def leerArchivo(self):
        try:
            n_archivo = self.txt_name.text() + ".txt"
            archivo = open("Archivos/"+ n_archivo)
            contenido = archivo.readlines()
            return contenido
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())