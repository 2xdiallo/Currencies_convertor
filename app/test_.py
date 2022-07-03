from PySide2 import QtWidgets


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_devise = QtWidgets.QComboBox()
        self.spb_montant = QtWidgets.QSpinBox()
        self.btt_inverser = QtWidgets.QPushButton("Inverser les devises ")

        self.layout.addWidget(self.cbb_devise)
        self.layout.addWidget(self.spb_montant)



app = QtWidgets.QApplication([])

window = App()

window.windowTitle = "disllo"
window.show()
app.exec_()






            