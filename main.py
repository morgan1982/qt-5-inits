import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDialog


class Demo(QMainWindow):

    def __init__(self):
        super().__init__()

        # menubar
        bar = self.menuBar() # creates an instance of the menubar
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')

        # create actions for the menu items
        save_action = QAction('Save', self) # needs a ref to the widget(self)
        save_action.setShortcut('Ctrl+S')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+Q')

        select_all = QAction('Select', self)

        find_device = QAction('Find Device', self)
        find_ticket = QAction('Find Ticket', self)

        # add action to the menu
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        find_menu = edit.addMenu('Find')
        find_menu.addAction(find_device)
        find_menu.addAction(find_ticket)


        edit.addAction(select_all)

        # events
        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.selected)

        self.setWindowTitle("demo 1")
        self.resize(600, 400)
        self.show()


    def quit_trigger(self):
        print('exit system')
        dialog = QDialog()
        dialog.setWindowTitle('pes mas')
        # dialog.setGeometry(100, 200, 800, 600)
        dialog.show()
        # qApp.quit()

    def selected(self, q):
        text = q.text()
        print(text + ' was selected')


app = QApplication(sys.argv)
menus = Demo()
sys.exit(app.exec_())