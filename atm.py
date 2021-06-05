import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class IntroWindow(QWidget):
    def __init__(self, parent=None):
        super(IntroWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("ATM")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(50, 50, 400, 515)
        self.text = QLabel("Please insert \n your card", self)
        self.text.setGeometry(5, 5, 380, 215)
        self.text.setFont(QFont('Arial', 45))
        self.text.setAlignment(Qt.AlignCenter)
        self.img = QLabel("", self)
        self.pixmap = QPixmap('img.png')
        self.img.setPixmap(self.pixmap)
        self.img.setAlignment(Qt.AlignCenter)
        self.img.setGeometry(75, 230, 250, 245)
        self.push_start = QPushButton("Start", self)
        self.push_start.setGeometry(125, 350, 150, 75)
        self.push_start.setStyleSheet("QPushButton::focus { background-color : red; color : white; font-size : 25px}")
        self.show()


class ATMPINWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMPINWindow, self).__init__(parent)
        self.text = QLabel("Enter your PIN", self)
        self.text.setGeometry(15, 5, 380, 100)
        self.text.setFont(QFont('Arial', 30))
        self.text.setAlignment(Qt.AlignCenter)
        self.label = QLineEdit(self)
        self.label.setGeometry(15, 85, 370, 80)
        self.label.setStyleSheet("QLabel{ border : 4px solid black; background : white; }")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 45))
        self.push1 = QPushButton("1", self)
        self.push1.setGeometry(15, 175, 120, 70)
        self.push1.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push2 = QPushButton("2", self)
        self.push2.setGeometry(140, 175, 120, 70)
        self.push2.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push3 = QPushButton("3", self)
        self.push3.setGeometry(265, 175, 120, 70)
        self.push3.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push4 = QPushButton("4", self)
        self.push4.setGeometry(15, 250, 120, 70)
        self.push4.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push5 = QPushButton("5", self)
        self.push5.setGeometry(140, 250, 120, 70)
        self.push5.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push6 = QPushButton("6", self)
        self.push6.setGeometry(265, 250, 120, 70)
        self.push6.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push7 = QPushButton("7", self)
        self.push7.setGeometry(15, 325, 120, 70)
        self.push7.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push8 = QPushButton("8", self)
        self.push8.setGeometry(140, 325, 120, 70)
        self.push8.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push9 = QPushButton("9", self)
        self.push9.setGeometry(265, 325, 120, 70)
        self.push9.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push_del = QPushButton("Del", self)
        self.push_del.setGeometry(15, 400, 120, 70)
        self.push_del.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push0 = QPushButton("0", self)
        self.push0.setGeometry(140, 400, 120, 70)
        self.push0.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push_done = QPushButton("Done", self)
        self.push_done.setGeometry(265, 400, 120, 70)
        self.push_done.setStyleSheet("QPushButton::focus { background-color : red; }")


class ATMActionWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMActionWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("ATM")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(50, 50, 400, 435)
        self.text = QLabel("Choose an action", self)
        self.text.setGeometry(5, 5, 380, 100)
        self.text.setFont(QFont('Arial', 35))
        self.text.setAlignment(Qt.AlignCenter)
        self.push_cash = QPushButton("Cash Withdrawal", self)
        self.push_cash.setGeometry(20, 85, 360, 80)
        self.push_cash.setStyleSheet("QPushButton::hover { background-color : red; color : white; font-size : 20px }"
                                     "QPushButton { color : black; font-size : 20px }")
        self.push_bal = QPushButton("Balance Enquiry", self)
        self.push_bal.setGeometry(20, 170, 360, 80)
        self.push_bal.setStyleSheet("QPushButton::hover { background-color : red; color : white; font-size : 20px }"
                                    "QPushButton { color : black; font-size : 20px }")
        self.push_trans = QPushButton("Transaction Details", self)
        self.push_trans.setGeometry(20, 255, 360, 80)
        self.push_trans.setStyleSheet("QPushButton::hover { background-color : red; color : white; font-size : 20px }"
                                      "QPushButton { color : black; font-size : 20px }")
        self.push_cancel = QPushButton("Cancel", self)
        self.push_cancel.setGeometry(20, 340, 360, 80)
        self.push_cancel.setStyleSheet("QPushButton::hover { background-color : red; color : white; font-size : 20px }"
                                       "QPushButton { color : black; font-size : 20px }")
        self.show()


class ATMCashWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMCashWindow, self).__init__(parent)
        self.text = QLabel("Enter amount", self)
        self.text.setGeometry(15, 5, 380, 100)
        self.text.setFont(QFont('Arial', 30))
        self.text.setAlignment(Qt.AlignCenter)
        self.label = QLineEdit(self)
        self.label.setGeometry(15, 85, 370, 80)
        self.label.setStyleSheet("QLabel{ border : 4px solid black; background : white; }")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 45))
        self.label.setText("₹")
        self.push1 = QPushButton("1", self)
        self.push1.setGeometry(15, 175, 120, 70)
        self.push1.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push1.setFocus()
        self.push2 = QPushButton("2", self)
        self.push2.setGeometry(140, 175, 120, 70)
        self.push2.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push3 = QPushButton("3", self)
        self.push3.setGeometry(265, 175, 120, 70)
        self.push3.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push4 = QPushButton("4", self)
        self.push4.setGeometry(15, 250, 120, 70)
        self.push4.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push5 = QPushButton("5", self)
        self.push5.setGeometry(140, 250, 120, 70)
        self.push5.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push6 = QPushButton("6", self)
        self.push6.setGeometry(265, 250, 120, 70)
        self.push6.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push7 = QPushButton("7", self)
        self.push7.setGeometry(15, 325, 120, 70)
        self.push7.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push8 = QPushButton("8", self)
        self.push8.setGeometry(140, 325, 120, 70)
        self.push8.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push9 = QPushButton("9", self)
        self.push9.setGeometry(265, 325, 120, 70)
        self.push9.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push_del = QPushButton("Del", self)
        self.push_del.setGeometry(15, 400, 120, 70)
        self.push_del.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push0 = QPushButton("0", self)
        self.push0.setGeometry(140, 400, 120, 70)
        self.push0.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.push_done = QPushButton("Done", self)
        self.push_done.setGeometry(265, 400, 120, 70)
        self.push_done.setStyleSheet("QPushButton::focus { background-color : red; }")
        self.show()


class ATMBalanceWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMBalanceWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("ATM")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(50, 50, 400, 515)
        self.text = QLabel("Your account \n balance is \n ₹25938", self)
        self.text.setGeometry(5, 75, 380, 215)
        self.text.setFont(QFont('Arial', 35))
        self.text.setAlignment(Qt.AlignCenter)
        self.img = QLabel("", self)
        self.push_done = QPushButton("Done", self)
        self.push_done.setGeometry(125, 350, 150, 75)
        self.push_done.setStyleSheet("QPushButton::focus { background-color : red; color : white; font-size : 25px}")
        self.show()


class ATMTransactionWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMTransactionWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("ATM")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(50, 50, 400, 515)
        self.text = QLabel("Transaction details", self)
        self.text.setGeometry(5, 5, 380, 100)
        self.text.setFont(QFont('Arial', 30))
        self.text.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel("+₹500 A/C:864729402955\n 01/06/2021 \n -₹2000 A/C:104850630274\n 31/05/2021 \n"
                            "+₹10000 A/c:105304967234\n 31/05/2021 \n +₹100 A/c:283924239281\n 29/05/2021", self)
        self.text2.setGeometry(5, 100, 380, 215)
        self.text2.setFont(QFont('Arial', 15))
        self.text2.setAlignment(Qt.AlignCenter)
        self.push_done = QPushButton("Done", self)
        self.push_done.setGeometry(125, 350, 150, 75)
        self.push_done.setStyleSheet("QPushButton::focus { background-color : red; color : white; font-size : 25px}")
        self.show()


class ATMCollectCashWindow(QWidget):
    def __init__(self, parent=None):
        super(ATMCollectCashWindow, self).__init__(parent)
        self.label = QLabel(self)
        self.setWindowTitle("ATM")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(50, 50, 400, 515)
        self.text = QLabel("Please collect \n your cash", self)
        self.text.setGeometry(5, 75, 380, 215)
        self.text.setFont(QFont('Arial', 35))
        self.text.setAlignment(Qt.AlignCenter)
        self.img = QLabel("", self)
        self.push_done = QPushButton("Done", self)
        self.push_done.setGeometry(125, 350, 150, 75)
        self.push_done.setStyleSheet("QPushButton::focus { background-color : red; color : white; font-size : 25px}")
        self.show()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 475)
        self.setFixedSize(400, 475)
        self.startIntro()

    def startIntro(self):
        self.IntroWindow = IntroWindow(self)
        self.setWindowTitle("ATM Intro Window")
        self.setCentralWidget(self.IntroWindow)
        self.IntroWindow.push_start.clicked.connect(self.startPIN)
        self.IntroWindow.img.lower()
        self.show()

    def startPIN(self):
        self.Window = ATMPINWindow(self)
        self.setWindowTitle("ATM PIN Window")
        self.setCentralWidget(self.Window)
        self.Window.push_done.clicked.connect(self.startAction)
        self.Window.push1.clicked.connect(self.action1)
        self.Window.push2.clicked.connect(self.action2)
        self.Window.push3.clicked.connect(self.action3)
        self.Window.push4.clicked.connect(self.action4)
        self.Window.push5.clicked.connect(self.action5)
        self.Window.push6.clicked.connect(self.action6)
        self.Window.push7.clicked.connect(self.action7)
        self.Window.push8.clicked.connect(self.action8)
        self.Window.push9.clicked.connect(self.action9)
        self.Window.push0.clicked.connect(self.action0)
        self.Window.push_del.clicked.connect(self.action_del)
        self.show()

    def startAction(self):
        self.ActionWindow = ATMActionWindow(self)
        self.setWindowTitle("ATM Action Window")
        self.setCentralWidget(self.ActionWindow)
        self.ActionWindow.push_cash.clicked.connect(self.startAmount)
        self.ActionWindow.push_bal.clicked.connect(self.startBalance)
        self.ActionWindow.push_trans.clicked.connect(self.startTransaction)
        self.ActionWindow.push_cancel.clicked.connect(self.startIntro)
        self.show()

    def startAmount(self):
        self.Window = ATMCashWindow(self)
        self.setWindowTitle("ATM Cash Window")
        self.setCentralWidget(self.Window)
        self.Window.push_done.clicked.connect(self.startCashCollect)
        self.Window.push1.clicked.connect(self.action1)
        self.Window.push2.clicked.connect(self.action2)
        self.Window.push3.clicked.connect(self.action3)
        self.Window.push4.clicked.connect(self.action4)
        self.Window.push5.clicked.connect(self.action5)
        self.Window.push6.clicked.connect(self.action6)
        self.Window.push7.clicked.connect(self.action7)
        self.Window.push8.clicked.connect(self.action8)
        self.Window.push9.clicked.connect(self.action9)
        self.Window.push0.clicked.connect(self.action0)
        self.Window.push_del.clicked.connect(self.action_del)
        self.show()

    def startBalance(self):
        self.BalanceWindow = ATMBalanceWindow(self)
        self.setWindowTitle("ATM Balance Window")
        self.setCentralWidget(self.BalanceWindow)
        self.BalanceWindow.push_done.clicked.connect(self.startIntro)
        self.show()

    def startTransaction(self):
        self.TransactionWindow = ATMTransactionWindow(self)
        self.setWindowTitle("ATM Transaction Window")
        self.setCentralWidget(self.TransactionWindow)
        self.TransactionWindow.push_done.clicked.connect(self.startIntro)
        self.show()

    def startCashCollect(self):
        self.CashCollectWindow = ATMCollectCashWindow(self)
        self.setWindowTitle("ATM Cash collect Window")
        self.setCentralWidget(self.CashCollectWindow)
        self.CashCollectWindow.push_done.clicked.connect(self.startIntro)
        self.show()

    def action0(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "0")

    def action1(self):
        print('comes here')
        text = self.Window.label.text()
        self.Window.label.setText(text + "1")

    def action2(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "2")

    def action3(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "3")

    def action4(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "4")

    def action5(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "5")

    def action6(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "6")

    def action7(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "7")

    def action8(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "8")

    def action9(self):
        text = self.Window.label.text()
        self.Window.label.setText(text + "9")

    def action_del(self):
        text = self.Window.label.text()
        print(text[:len(text) - 1])
        self.Window.label.setText(text[:len(text) - 1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
