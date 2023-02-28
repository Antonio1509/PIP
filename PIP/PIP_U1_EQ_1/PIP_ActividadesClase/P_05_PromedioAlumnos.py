import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_05_PromedioAlumnos.ui" # Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_add.clicked.connect(self.agregar)
        self.btn_prom.clicked.connect(self.promedio)

        self.calificaciones = []

    # Área de los slots
    def agregar(self):
        num = float(self.txt_cal.text())
        self.calificaciones.append(num)
        print(self.calificaciones)

    def promedio(self):
        prom =  sum(self.calificaciones) / len(self.calificaciones)
        print(prom)
        self.txt_prom.setText(str(prom))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())