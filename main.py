import sys, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from ui.login import Ui_MainWindow
from ui.answer_login import Ui_Form_answer_login
from ui.admin import Ui_MainWindow_admin
from ui.manager import Ui_MainWindow_manager

con = sqlite3.connect("hotel.db")  # Подключение к БД

cur = con.cursor()  # Создание курсора
pas = ""
log = pas
result = 0
zifer = 0
login_answer_text = ""


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_cancel.clicked.connect(self.cancel)
        self.pushButton_log_in.clicked.connect(self.log_in)

    def cancel(self):
        self.close()

    def log_in(self):
        log = self.lineEdit_user_name.text()
        pas = self.lineEdit_password.text()
        zifer = "SELECT * FROM user_admin WHERE password = '" + pas + "' and login = '" + log + "'"
        result_admin = cur.execute(zifer).fetchall()
        zifer = "SELECT * FROM user_manager WHERE password = '" + pas + "' and login = '" + log + "'"
        result_manager = cur.execute(zifer).fetchall()

        if (len(result_admin) == 0 and len(result_manager) == 0):
            zifer = "INSERT INTO wrong_login VALUES (0,'" + log + "', '" + pas + "', '0')"
            result_login = cur.execute(zifer)
            con.commit()
            self.ans_login = Login_form_wrong()
            self.ans_login.show()
        elif (len(result_admin)):
            self.ans_login = Login_form_admin()
            self.ans_login.show()
        else:
            self.ans_login = Login_form_manager()
            self.ans_login.show()


class Login_form_wrong(QWidget, Ui_Form_answer_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_user_type.setText("Не удалось авторизоваться")
        self.pushButton.setText("Вернуться")
        self.pushButton.clicked.connect(self.close)


class Login_form_admin(QWidget, Ui_Form_answer_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_user_type.setText("Вы администратор гостиницы")
        self.pushButton.setText("Продолжить")
        self.pushButton.clicked.connect(self.login_admin)

    def login_admin(self):
        self.adm = Admin()
        self.adm.show()

class Admin(QMainWindow,Ui_MainWindow_admin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Login_form_manager(QWidget, Ui_Form_answer_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_user_type.setText("Вы управляющий сетью гостиниц")
        self.pushButton.setText("Продолжить")
        self.pushButton.clicked.connect(self.login_manager)

        def login_manager(self):
            self.mang = Manager()
            self.mang.show()

class Manager(QMainWindow, Ui_MainWindow_manager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

con.close()
