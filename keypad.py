from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
keypad_value = ""


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		self.setWindowTitle("Python ")
		self.setGeometry(100, 100, 380, 420)
		self.UiComponents()
		self.show()

	def UiComponents(self):

		self.label = QLabel(self)
		self.label.setGeometry(5, 5, 370, 70)
		self.label.setWordWrap(True)
		self.label.setStyleSheet("QLabel{ border : 4px solid black; background : white; }")
		self.label.setAlignment(Qt.AlignRight)
		self.label.setFont(QFont('Arial', 45))

		push1 = QPushButton("1", self)
		push1.setGeometry(5, 80, 120, 80)
		push1.setStyleSheet("QPushButton::focus { background-color : red; }")
		push2 = QPushButton("2", self)
		push2.setGeometry(130, 80, 120, 80)
		push2.setStyleSheet("QPushButton::focus { background-color : red; }")
		push3 = QPushButton("3", self)
		push3.setGeometry(255, 80, 120, 80)
		push3.setStyleSheet("QPushButton::focus { background-color : red; }")
		push4 = QPushButton("4", self)
		push4.setGeometry(5, 165, 120, 80)
		push4.setStyleSheet("QPushButton::focus { background-color : red; }")
		push5 = QPushButton("5", self)
		push5.setGeometry(130, 165, 120, 80)
		push5.setStyleSheet("QPushButton::focus { background-color : red; }")
		push6 = QPushButton("6", self)
		push6.setGeometry(255, 165, 120, 80)
		push6.setStyleSheet("QPushButton::focus { background-color : red; }")
		push7 = QPushButton("7", self)
		push7.setGeometry(5, 250, 120, 80)
		push7.setStyleSheet("QPushButton::focus { background-color : red; }")
		push8 = QPushButton("8", self)
		push8.setGeometry(130, 250, 120, 80)
		push8.setStyleSheet("QPushButton::focus { background-color : red; }")
		push9 = QPushButton("9", self)
		push9.setGeometry(255, 250, 120, 80)
		push9.setStyleSheet("QPushButton::focus { background-color : red; }")
		push_del = QPushButton("Del", self)
		push_del.setGeometry(5, 335, 120, 80)
		push_del.setStyleSheet("QPushButton::focus { background-color : red; }")
		push0 = QPushButton("0", self)
		push0.setGeometry(130, 335, 120, 80)
		push0.setStyleSheet("QPushButton::focus { background-color : red; }")
		push_done = QPushButton("Done", self)
		push_done.setGeometry(255, 335, 120, 80)
		push_done.setStyleSheet("QPushButton::focus { background-color : red; }")

		push0.clicked.connect(self.action0)
		push1.clicked.connect(self.action1)
		push2.clicked.connect(self.action2)
		push3.clicked.connect(self.action3)
		push4.clicked.connect(self.action4)
		push5.clicked.connect(self.action5)
		push6.clicked.connect(self.action6)
		push7.clicked.connect(self.action7)
		push8.clicked.connect(self.action8)
		push9.clicked.connect(self.action9)
		push_done.clicked.connect(self.action_done)
		push_del.clicked.connect(self.action_del)

	def action0(self):
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		text = self.label.text()
		self.label.setText(text + "9")

	def action_done(self):
		global keypad_value
		keypad_value = self.label.text()
		self.label.setText("")
		self.close()

	def action_del(self):
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])


def open_keypad():
	app = QApplication(sys.argv)
	window = Window()
	app.exec()
	return keypad_value
