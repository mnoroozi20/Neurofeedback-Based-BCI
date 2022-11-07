import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        #self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Window")
        self.setStyleSheet('background: #505050')
        self.stage = 3
        self.home()

    def home(self):
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        label1 = QtWidgets.QLabel('Patient:')
        label1.setFixedWidth(50)
        label1.setStyleSheet('font-size: 15px')

        self.line = QtWidgets.QLineEdit(self)
        self.line.setFixedWidth(200)
        self.line.setStyleSheet('background: #EEEEEE; margin-right: 20px')
        
        start_btn = QtWidgets.QPushButton('Start', self)
        start_btn.setFixedWidth(75)
        start_btn.setStyleSheet('background: #228C22')
        start_btn.clicked.connect(self.func) 

        stop_btn = QtWidgets.QPushButton('Stop', self)
        stop_btn.setFixedWidth(75)
        stop_btn.setStyleSheet('background: #B80F0A')
        stop_btn.clicked.connect(self.func) 

        label2 = QtWidgets.QLabel('Phase:')
        label2.setFixedWidth(50)
        label2.setStyleSheet('font-size: 15px')

        combobox = QtWidgets.QComboBox(self)
        combobox.addItem('Pre-Evaluation')
        combobox.addItem('Neurofeedback')
        combobox.addItem('Post-Evaluation')
        combobox.setFixedWidth(100)
        combobox.setStyleSheet('background: #FFFFFF; margin-left: 1px; margin-right: 1px')

        label3 = QtWidgets.QLabel('Stage:')
        label3.setFixedWidth(50)
        label3.setStyleSheet('font-size: 15px')

        image = QtGui.QPixmap("C:/Users/tnlab/Desktop/Neurofeedback-Project/Asssets/BlockLoad" + str(self.stage) +"_5.png").scaled(175,175, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        block = QtWidgets.QLabel()
        block.setPixmap(image)
        block.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        block.setFixedWidth(175)

        grid.addWidget(label1,0,0)
        grid.addWidget(self.line,0,1)
        grid.addWidget(start_btn,0,2)
        grid.addWidget(stop_btn,0,3)
        grid.addWidget(label2,1,0)
        grid.addWidget(combobox,1,1)
        grid.addWidget(label3,2,0)
        grid.addWidget(block,2,1)
        self.show()

    def func(self):
        print(self.line.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())