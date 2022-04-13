from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        # Set the window open location and size
        # win.setGeometry(xpos, ypos, width, height)
        self.setGeometry(900, 300, 300, 300)
        # Title of window.
        self.setWindowTitle("Basic window")
        self.button_count = 0

    def initUI(self):
        # Create a label in the window we made.
        self.label = QtWidgets.QLabel(self)
        # Text of the label
        self.label.setText("My First Label.")
        # Where the label should show up in the window.
        self.label.move(50, 50)

        # Create a button
        self.b1 = QtWidgets.QPushButton(self)
        # set location of the button.
        self.b1.move(50, 75)
        # text of the button
        self.b1.setText("This is a button")
        # mapping a function to a button
        self.b1.clicked.connect(self.clicked)


    def clicked(self):
        # changes the label when the button is pressed.
        self.button_count += 1
        self.label.setText(f"You pressed the button {self.button_count} times!")
        self.update()

    def update(self):
        # updates the size of the label.
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    # Allows Window to Show.
    win.show()
    # Allows for clean exit of the application.
    sys.exit(app.exec_())

window()