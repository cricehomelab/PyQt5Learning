# using this example from https://www.pythonguis.com/tutorials/qscrollarea/ to mess around with the code to get a
# working scrolling area. 

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.label_list = ["first label", "second label", "third label", "yes", "no", "magic", "spark", "thirteen",
                           "hello", "world", "This", "is", "a", "list", "of", "labels", "I", "typed", "in", "to",
                           "make", "a", "scroll", "area", "work", "for", "me", "I", "needed", "to", "add", "more",
                           "for", "this", "to", "scroll", "like", "I", "want", "it", "to"]
        print(self.label_list)
        self.initUI()


    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        print(self.label_list)
        for num, i in enumerate(self.label_list):
            object = QPushButton(i)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()