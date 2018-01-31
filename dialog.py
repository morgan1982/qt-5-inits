import sys
from pprint import pprint
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
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
        menuBar = self.menuBar()
        file_menu = menuBar.addMenu('&File')
        # menuBar.setNativeMenuBar(False) # on mac only
        self.setGeometry(900, 200, 600, 400)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pprint("input params = " +  str(sys.argv))
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
