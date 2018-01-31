import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QAction, QWidget, QDialog, QMainWindow, qApp, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
# from structure import Ui_Dialog
# from widget import Ui_Form
from main_ex import Ui_MainWindow


class AppWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__()
        # self.ui = Ui_Dialog()
        # self.ui = Ui_Form()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.btn_1 = QPushButton('power')
        self.btn_1.clicked.connect(self.action1)
        self.number_of_pressed = 0

        self.init_ui()

        self.x = 1

        self.show()

    def init_ui(self):
        self.setWindowTitle('operator')
        self.statusBar().showMessage('operating')

        label1 = QLabel('This is label1', self)
        label1.move(100, 100)

        # box layouts
        ok_btn = QPushButton("Ok")
        cancel_btn = QPushButton("Cancel")

        label2 = QLabel("second label")
        label2.setAlignment(QtCore.Qt.AlignCenter)

        h_box = QHBoxLayout()
        h_box.addWidget(label2)
        h_box.addStretch(1)
        h_box.addWidget(ok_btn)
        h_box.addWidget(cancel_btn)
        h_box.addStretch(1)

        # calculator ex grid layout
        grid_layout = QGridLayout()
        values = [
            '1', '2', '3', '-',
            '4', '5', '6', '*',
            '7', '8', '9', '/',
            '0', '.', '=', '+', ]
        positions = [(i, j) for i in range(4) for j in range(4)]
        # print("positions = ", positions)
        # print("position = ", position)
        print(list(zip(positions, values)))

        for position, value in zip(positions, values):
            # print("position = ", position)
            # print("value = ", value)
            if value == '':
                continue
            button = QPushButton(value)
            grid_layout.addWidget(button, *position)

        self.ui.v_layout.addLayout(h_box)
        self.ui.v_layout.addLayout(grid_layout)
        # self.ui.v_layout.addWidget(ok_btn)

        # second layout
        label1 = QLabel('products name')
        txt_title = QLineEdit()
        txt_title.setPlaceholderText('enter your product')
        txt_review = QTextEdit()
        txt_review.setPlaceholderText("Enter your opinion")

        grid_layout2 = QGridLayout()
        grid_layout2.setSpacing(10)

        grid_layout2.addWidget(label1, 0, 0)  # row - column
        grid_layout2.addWidget(txt_title, 0, 1)
        print(self.x)
        grid_layout2.addWidget(txt_review, 2, 1, 5, 1)

        btn_2 = QPushButton('num 2')
        btn_2.clicked.connect(self.dialog1)
        grid_layout2.addWidget(self.btn_1, 1, 0)
        grid_layout2.addWidget(btn_2, 2, 0)

        self.ui.v_layout2.addLayout(grid_layout2)

        menuBar = self.menuBar()
        file_menu = menuBar.addMenu('&File')

        # actions
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Program')
        exit_action.triggered.connect(qApp.quit)

        # toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)
        file_menu.addAction(exit_action)

        self.ui.line_edit1.setPlaceholderText('enter the year')

        # menuBar.setNativeMenuBar(False) # on mac only
        self.setGeometry(900, 200, 800, 600)

    def action1(self):
        print('btn 1 clicked')
        sender = self.sender()
        print(sender.text())
        self.number_of_pressed += 1
        print(self.number_of_pressed)

    def dialog1(self):
        print('dialog1')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pprint("input params = " + str(sys.argv))
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
