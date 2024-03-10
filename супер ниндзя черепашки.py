from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)
from PyQt5 import QtGui
import pywinstyles

stfb = """
    QPushButton {
        color:blue;
        border-color: white;
        border-radius: 5px;
        border-width:1px;
        padding:10 px;
        border-style: Win7;
        font-weight: 600;
        font-size: 30px;
    }
    QPushButton:hover {
        color:green;
        border: 1px solid white;
        font-weight: 700;
        
    }
    QPushButton:focus {
        color:red;
        border: 1px solid gray;
        border-color: gray;
    }
    """

app = QApplication([])
window = QWidget()
window.setStyleSheet("background:yellow;")
layout = QVBoxLayout()

label = QLabel("Тут")

l_i = QLabel("хз как, но название есть")
l_i.setStyleSheet("color:blue;")
r = 0
t = 0

def rub(r):
    r = int(input_image.text())
    re = r/500
    label.setText(str(re))
def dol(t):
    t = int(inputа.text())
    re2 = t*500
    label.setText(str(re2))


i_r = QLabel()

p_c = QLabel("Здесь")
p_c = QPushButton()

window.setWindowTitle('Как фрилансить и зарабатывать миллион биткоинов в секунду?')
window.setWindowIcon(QtGui.QIcon('карты.png'))
pywinstyles.apply_style(window, 'native')


input_image = QLineEdit()
input_image.setStyleSheet('color:white;border:2px solid gray;padding: 5px;font-size:30px')
input_image.setPlaceholderText('хахаха, тут рубли, а ты повёлся!')
layout.addWidget(input_image)

inputа = QLineEdit()
inputа.setStyleSheet('color:white;border:2px solid gray;padding: 5px;font-size:30px')
inputа.setPlaceholderText('хахаха, тут долары, а ты повёлся!')
layout.addWidget(inputа)

r_t_d = QPushButton('перевод в доляры')
layout.addWidget(r_t_d)
r_t_d.setStyleSheet(stfb)
r_t_d.clicked.connect(
    lambda: rub(i_r))

d_t_r = QPushButton('щвылщвлаы')
layout.addWidget(d_t_r)
d_t_r.setStyleSheet(stfb)
d_t_r.clicked.connect(
    lambda: dol(i_r))

layout.addWidget(label)


window.setLayout(layout)
window.show()
window.resize(900,200)
app.exec_()