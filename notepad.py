import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()

        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('clear')
        self.save_btn = QPushButton('save')
        self.open_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)

        v_layout.addWidget(self.text)
        v_layout.addLayout(h_layout)

        self.save_btn.clicked.connect(self.save_text)
        self.clr_btn.clicked.connect(self.clear_text)
        self.open_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle("text editor")

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)
    
    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

app = QApplication(sys.argv)
writer = Notepad()
sys.exit(app.exec_())


        
    