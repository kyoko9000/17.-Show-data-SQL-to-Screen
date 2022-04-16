#no need to install anything
import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
# just change the name
from gui import Ui_MainWindow

# pip install mysql.connector-python
import mysql.connector
db = mysql.connector.connect(user='root', password='1234',
                             host='127.0.0.1', database='new_database')

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut an
        self.uic.Button_load_data.clicked.connect(self.load_data)
    def load_data(self):
        print("ready")
        while True:
            print("run")
            if QWidget.QCloseEvent():
                break

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())