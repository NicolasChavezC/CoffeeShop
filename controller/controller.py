from PyQt6 import QtWidgets, uic

class LoginController:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_cff_login.clicked.connect(self.handle_login)
    def handle_login(self):
        username = self.window.txt_user.text()
        password = self.window.txt_pass.text()
        if username == "asd" and password == "asd":
            self.window.login_successful.emit()
        else:
            QtWidgets.QMessageBox.warning(self.window, "Coffee Talk - ERROR","Login keys incorrect")

class Main:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_cff_Menu_Main.clicked.connect(self.main_to_menu)
        self.window.btn_cff_Menu_Main_Ad.clicked.connect(self.main_to_menu)
        self.window.btn_cff_Report_Main.clicked.connect(self.main_to_report)
    def main_to_menu(self):
        self.window.move_main_to_menu.emit()
    def main_to_report(self):
        self.window.move_main_to_report.emit()

class Menu:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_ct_Main_Menu.clicked.connect(self.menu_to_main)
        self.window.btn_cff_Report_Menu.clicked.connect(self.menu_to_report)
    def menu_to_main(self):
        self.window.move_menu_to_main.emit()
    def menu_to_report(self):
        self.window.move_menu_to_report.emit()

class Report:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_ct_Main_Report.clicked.connect(self.report_to_main)
        self.window.btn_cff_Menu_Report.clicked.connect(self.report_to_menu)
    def report_to_main(self):
        self.window.move_report_to_main.emit()
    def report_to_menu(self):
        self.window.move_report_to_menu.emit()