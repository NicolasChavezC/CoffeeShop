from PyQt6 import QtWidgets, uic
import sys
from controller.controller import LoginController
from controller.controller import Main_To_Menu
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class coffee_login(QtWidgets.QMainWindow):
    login_successful = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, self)

class coffee_main(QtWidgets.QDialog):
    move_main_to_menu = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui", self)
        self.controller = Main_To_Menu(self, self)

class coffee_menu(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/menu.ui", self)

class coffee_report(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/report.ui", self)

class AppManager:
    def __init__(self):
        self.coffee_login = coffee_login()
        self.coffee_main = coffee_main()
        self.coffee_menu = coffee_menu()
        self.coffee_report = coffee_report()
        self.coffee_login.show()
        self.coffee_login.login_successful.connect(self.show_main_window)
        self.coffee_main.move_main_to_menu.connect(self.menu_to_main)
    def show_main_window(self):
        self.coffee_main.show()
        self.coffee_login.close()
    def menu_to_main(self):
        self.coffee_menu.show()
        self.coffee_main.close()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())