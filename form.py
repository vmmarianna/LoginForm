from PyQt5 import QtWidgets
from mainui import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
import sqlite3
from utils import *

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.con = sqlite3.connect('database.db')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.SignIn_btn.clicked.connect(self.signin)
        self.ui.SignUp_btn.clicked.connect(self.signup)



    def signup(self):
        cur = self.con.cursor()
        name=self.ui.Name_edit.text()
        midname = self.ui.Middle_Name_edit.text()
        surname = self.ui.Surname_edit.text()
        bdate = self.ui.Birthday_edit.text()
        #print(bdate)
        rgdate = get_current_time()
        #print(rgdate)
        email = self.ui.Email_edit.text()
        phone = self.ui.Phone_edit.text()
        login=self.ui.Login_edit.text()
        passwd=get_hash(self.ui.Password_edit.text())

        SQL = f"""
        insert into User(Name,Middle_name,Surname,Birthdate,Reg_date,Email,Phone) VALUES('{name}','{midname}','{surname}','{bdate}','{rgdate}','{email}',{phone});
        """
        #print(SQL)
        cur.execute(SQL)
        SQL=f"""insert into secret(Login,Password,userid) values('{login}','{passwd}',{cur.lastrowid -1})"""
        #print(SQL)
        cur.execute(SQL)
        self.con.commit()


    def signin(self):
        login = self.ui.Login_edit_2.text()
        passwd = get_hash(self.ui.Password_edit_2.text())
        cur = self.con.cursor()
        cur.execute(f"""select * from secret where Login = "{login}" and Password = "{passwd}";""")
        if len(cur.fetchall()) > 0:
            print('Login successful')
        else:
            print("Login Failed")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())