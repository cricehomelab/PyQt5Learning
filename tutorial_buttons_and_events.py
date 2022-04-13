from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


def clicked():
    print("button clicked!")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # Set the window open location and size
    # win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(900, 300, 300, 300)
    # Title of window.
    win.setWindowTitle("Basic window")

    # Create a label in the window we made.
    label = QtWidgets.QLabel(win)
    # Text of the label
    label.setText("My First Label.")
    # Where the label should show up in the window.
    label.move(50, 50)

    # Create a button
    b1 = QtWidgets.QPushButton(win)
    # text of the button
    b1.setText("This is a button")
    # mapping a function to a button
    b1.clicked.connect(clicked)

    # Allows Window to Show.
    win.show()
    # Allows for clean exit of the application.
    sys.exit(app.exec_())

window()