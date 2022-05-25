import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.math_eval = ''
        self.display = ''
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi('calc3.ui')
        self.ui.show()

    def set(self):
        self.ui.p_dote.clicked.connect(lambda: self.click_num('.'))
        self.ui.p_0.clicked.connect(lambda: self.click_num(0))
        self.ui.p_1.clicked.connect(lambda: self.click_num(1))
        self.ui.p_2.clicked.connect(lambda: self.click_num(2))
        self.ui.p_3.clicked.connect(lambda: self.click_num(3))
        self.ui.p_4.clicked.connect(lambda: self.click_num(4))
        self.ui.p_5.clicked.connect(lambda: self.click_num(5))
        self.ui.p_6.clicked.connect(lambda: self.click_num(6))
        self.ui.p_7.clicked.connect(lambda: self.click_num(7))
        self.ui.p_8.clicked.connect(lambda: self.click_num(8))
        self.ui.p_9.clicked.connect(lambda: self.click_num(9))
        self.ui.p_minus.clicked.connect(lambda: self.click_action('-'))
        self.ui.p_plus.clicked.connect(lambda: self.click_action('+'))
        self.ui.p_equal.clicked.connect(lambda: self.get_result())
        self.ui.p_divide.clicked.connect(lambda: self.click_action('/'))
        self.ui.p_multiply.clicked.connect(lambda: self.click_action('*'))
        self.ui.p_c.clicked.connect(lambda: self.reset_all())

    def click_num(self, num):
        self.display = self.display + str(num)
        self.ui.label.setText(self.display)

    def reset_display(self):
        self.display = ''
        self.ui.label.setText('')

    def reset_all(self):
        self.display = ''
        self.math_eval = ''
        self.ui.label.setText('')

    def click_action(self, action):
        self.math_eval += self.display + action
        self.reset_display()

    def get_result(self):
        result = str(eval(self.math_eval + self.display))
        self.ui.label.setText(result)


app = QApplication(sys.argv)
ex = App()
app.exec_()

