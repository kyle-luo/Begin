# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        cryptokey = 50
        self.pbuttonName = QPushButton("Developer's Name")
        self.lineeditName = QLineEdit("")
        self.pbuttonSemester = QPushButton("Current Semester")
        self.lineeditSemester = QLineEdit("")
        self.pbutton0 = QPushButton("Open Input File")
        self.lineedit0 = QLineEdit("Input File Name")
        self.label1 = QLabel("Select a Function")
        self.pbutton1 = QPushButton("Character Count")
        self.lineedit1 = QLineEdit("")
        self.pbutton2 = QPushButton("Line Count")
        self.lineedit2 = QLineEdit("")
        self.pbutton3 = QPushButton("Unique Word Count")
        self.lineedit3 = QLineEdit("")
        self.pbutton4 = QPushButton("Average Characters Per Word")
        self.lineedit4 = QLineEdit("")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbuttonName)
        layout.addWidget(self.lineeditName)
        layout.addWidget(self.pbuttonSemester)
        layout.addWidget(self.lineeditSemester)       
        layout.addWidget(self.pbutton0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.label1)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        ck = cryptokey
        self.lineeditName.setFocus()
        self.connect(self.pbuttonName, SIGNAL("clicked()"),self.buttonNamePressed)
        self.connect(self.pbuttonSemester, SIGNAL("clicked()"),self.buttonSemesterPressed)
        self.connect(self.pbutton0, SIGNAL("clicked()"),self.button0Pressed)
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        s = chr(ck + 20) + chr(ck) + chr(ck-2) +chr(ck-1)+chr(ck+6)
        self.setWindowTitle(s)
    # Form Methods
    def buttonNamePressed(self):
        self.lineeditName.setText("My Name is Kaiyu Luo")
    def buttonSemesterPressed(self):
        self.lineeditSemester.setText("Current Semester is F2018")
    def button0Pressed(self):
        self.lineedit0.setText("File xxxx Opened")
    def button1Pressed(self):
        self.lineedit1.setText("xxxx alpha characters counted")
    def button2Pressed(self):
        self.lineedit2.setText("xxxx non empty lines counted")
    def button3Pressed(self):
        self.lineedit3.setText("xxxx words counted")
    def button4Pressed(self):
        self.lineedit4.setText("xxx occurrences of _ counted")
    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
