import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_07_LeerArchivo.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_read.clicked.connect(self.leer)

    # Área de los slots
    def leer(self):
        try:
            n_archivo = self.txt_name.text() + ".txt"
            archivo = open("Archivos/"+ n_archivo)
            contenido = archivo.readlines()
            texto = ""
            for linea in contenido:
                texto += linea
            self.txt_vista.setText(str(texto))
            print(contenido)
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())