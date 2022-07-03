"""
    Program in Graphical User Interface written in Python 3.7.3 which coverts Currencies  .

    Author : 2xdiallo
    email: dialload561@gmail.com
    Link_Github: https://github.com/2xdiallo/Currencies_convertor.git
    
"""


import PySide2
import currency_converter

from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de Devise by 2xdiallo")
        self.set_ui()
        self.set_default_values()
        self.set_style()
        self.resize(500,50)
        self.setWindowIcon(PySide2.QtGui.QIcon("C:\\Python_projects\\Projet_calculatrice\\app\icon.png") ) #("icon.png"))  PySide2.QtGui.QIcon
        self.set_connections()

    def set_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.cbb_deviseFrom = QtWidgets.QComboBox()
        self.spb_montantFrom = QtWidgets.QSpinBox()
        self.cbb_deviseTo = QtWidgets.QComboBox()
        self.spb_montantTo = QtWidgets.QSpinBox()
        self.btn_inverser = QtWidgets.QPushButton("Inverse_Devise")

        self.layout.addWidget(self.cbb_deviseFrom)
        self.layout.addWidget(self.spb_montantFrom)
        self.layout.addWidget(self.cbb_deviseTo)
        self.layout.addWidget(self.spb_montantTo)
        self.layout.addWidget(self.btn_inverser)



    def set_default_values(self):
        self.devises = sorted(list(self.c.currencies)) 
        self.cbb_deviseFrom.addItems(self.devises)
        self.cbb_deviseTo.addItems(self.devises)
        self.cbb_deviseFrom.setCurrentText("EUR")
        self.cbb_deviseTo.setCurrentText("EUR")


        self.spb_montantFrom.setRange(1,1000000)
        self.spb_montantTo.setRange(1,1000000)
        self.spb_montantFrom.setDisplayIntegerBase(10)
        self.spb_montantTo.setDisplayIntegerBase(10)
        self.spb_montantFrom.setSpecialValueText("0")
        self.spb_montantTo.setSpecialValueText("0")

    def set_style(self):
        self.setStyleSheet("""
        background-color : black ;
        color : white ;
        border : None
        
        """)


    def set_connections(self):
        self.cbb_deviseFrom.activated.connect(self.compute)
        self.cbb_deviseTo.activated.connect(self.compute)

        self.spb_montantFrom.valueChanged.connect(self.compute)
        self.spb_montantTo.valueChanged.connect(self.compute)
        self.btn_inverser.clicked.connect(self.inverser)

    def compute(self):
        montant = self.spb_montantFrom.value()
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()
        try:
            montant_converti = self.c.convert(montant,devise_from,devise_to)
        except :
            print("la conversion a echoue ...")
        else:
            self.spb_montantTo.setValue(montant_converti)


    def inverser(self):
        print("I inverse them ")
        devise_from = self.cbb_deviseFrom.currentText()
        devise_to = self.cbb_deviseTo.currentText()
        print(devise_from,"\n",devise_to)
        self.cbb_deviseFrom.setCurrentText(devise_to)
        self.cbb_deviseTo.setCurrentText(devise_from)
        self.compute()

#creer une instance de la classe QtWidgets.QApplication
app = QtWidgets.QApplication([]) #prend toujours une liste vide en parametre

window = App()
window.show()
app.exec_()





