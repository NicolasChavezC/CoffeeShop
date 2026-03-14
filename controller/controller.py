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

class Main_To_Menu:
    def __init__(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_cff_Menu_Main.clicked.connect(self.main_to_menu)
    def main_to_menu(self):
        self.window.move_main_to_menu.emit()