from PyQt6 import QtWidgets, uic
import sys
from controller.controller import LoginController
from controller.controller import Main
from controller.controller import Menu
from controller.controller import Report
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
    move_main_to_report = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main.ui", self)
        self.controller = Main(self, self)

class coffee_menu(QtWidgets.QDialog):
    move_menu_to_main = pyqtSignal()
    move_menu_to_report = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/menu.ui", self)
        self.controller = Menu(self, self)

class coffee_report(QtWidgets.QDialog):
    move_report_to_main = pyqtSignal()
    move_report_to_menu = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/report.ui", self)
        self.controller = Report(self, self)

class AppManager:
    def __init__(self):
        self.coffee_login = coffee_login()
        self.coffee_main = coffee_main()
        self.coffee_menu = coffee_menu()
        self.coffee_report = coffee_report()
        self.coffee_login.show()
        self.coffee_login.login_successful.connect(self.show_main_window)
        self.coffee_main.move_main_to_menu.connect(self.menu_to_main)
        self.coffee_main.move_main_to_report.connect(self.menu_to_report)
        self.coffee_menu.move_menu_to_main.connect(self.menu_to_main)
        self.coffee_menu.move_menu_to_report.connect(self.menu_to_report)
        self.coffee_report.move_report_to_main.connect(self.report_to_main)
        self.coffee_report.move_report_to_menu.connect(self.report_to_menu)
    def show_main_window(self):
        self.coffee_main.show()
        self.coffee_login.close()
    def menu_to_main(self):
        self.coffee_menu.show()
        self.coffee_main.close()
    def menu_to_report(self):
        self.coffee_report.show()
        self.coffee_menu.close()
    def report_to_main(self):
        self.coffee_main.show()
        self.coffee_report.close()
    def report_to_menu(self):
        self.coffee_menu.show()
        self.coffee_report.close()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())