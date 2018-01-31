import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication,QAction, QWidget, QDialog, QMainWindow, qApp, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
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
        self.init_ui()
        self.show()
        # self.ui.note_edit.setText('kolos')

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
        values = [
            '1', '2', '3', '-',
            '4', '5', '6', '*',
            '7', '8', '9', '/',
            '7', '8', '9', '/',
            '0', '.', '=', '+',                                       ]
        
        

        self.ui.v_layout.addLayout(h_box)
        # self.ui.v_layout.addWidget(ok_btn)

        

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

        # menuBar.setNativeMenuBar(False) # on mac only
        self.setGeometry(900, 200, 600, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pprint("input params = " +  str(sys.argv))
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
