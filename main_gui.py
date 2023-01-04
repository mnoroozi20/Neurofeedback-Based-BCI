import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import csv
import time
from os import listdir
from image_display import *


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("Main Window")
        self.setStyleSheet('background: #707070')
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        # Sub Window
        
        self.sub_window_active = False
        self.stage = 0
        self.home()

    def home(self):
        self.blocks = 0

        label1 = QtWidgets.QLabel('Patient:')
        label1.setFixedWidth(50)
        label1.setStyleSheet('font-size: 15px; ')

        self.patient_btn = QtWidgets.QPushButton('Add Patient Data', self)
        self.patient_btn.setFixedWidth(100)
        self.patient_btn.setStyleSheet('background: #1634EF')
        self.patient_btn.clicked.connect(self.add_patient_data)

        self.line = QtWidgets.QLineEdit(self)
        self.line.setFixedWidth(200)
        # label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.line.setStyleSheet('background: #EEEEEE; margin-right: 20px')

        self.start_btn = QtWidgets.QPushButton('Start', self)
        self.start_btn.setFixedWidth(75)
        self.start_btn.setStyleSheet('background: #228C22')
        self.start_btn.clicked.connect(self.run_next_stage)

        self.stop_btn = QtWidgets.QPushButton('Stop', self)
        self.stop_btn.setFixedWidth(75)
        self.stop_btn.setStyleSheet('background: #B80F0A')
        self.stop_btn.clicked.connect(self.func)

        self.label2 = QtWidgets.QLabel('Phase:')
        self.label2.setFixedWidth(50)
        self.label2.setStyleSheet('font-size: 15px')

        self.combobox = QtWidgets.QComboBox(self)
        self.combobox.addItem('Pre-Evaluation')
        self.combobox.addItem('Neurofeedback')
        self.combobox.addItem('Post-Evaluation')
        self.combobox.setFixedWidth(100)
        self.combobox.setStyleSheet('background: #FFFFFF; margin-left: 1px; margin-right: 1px')
        self.combobox.activated[str].connect(self.onStageChange)

        self.label3 = QtWidgets.QLabel('Stage:')
        self.label3.setFixedWidth(50)
        self.label3.setStyleSheet('font-size: 15px')

        self.image = QtGui.QPixmap("Asssets/BlockLoad0_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image1 = QtGui.QPixmap("Asssets/BlockLoad1_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image2 = QtGui.QPixmap("Asssets/BlockLoad2_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image3 = QtGui.QPixmap("Asssets/BlockLoad3_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image4 = QtGui.QPixmap("Asssets/BlockLoad4_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image5 = QtGui.QPixmap("Asssets/BlockLoad5_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image6 = QtGui.QPixmap("Asssets/BlockLoad6_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image7 = QtGui.QPixmap("Asssets/BlockLoad7_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image8 = QtGui.QPixmap("Asssets/BlockLoad8_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.block = QtWidgets.QLabel()
        self.block.setPixmap(self.image)
        self.block.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.block.setFixedWidth(300)
        self.block.setFixedHeight(50)

        self.grid.addWidget(label1, 0, 0)
        self.grid.addWidget(self.line, 0, 1)
        self.grid.addWidget(self.start_btn, 0, 2)
        self.grid.addWidget(self.stop_btn, 0, 3)
        self.grid.addWidget(self.patient_btn, 1, 1)
        self.grid.addWidget(self.label2, 2, 0)
        self.grid.addWidget(self.combobox, 2, 1)
        self.grid.addWidget(self.label3, 3, 0)
        self.grid.addWidget(self.block, 3, 1)
        self.show()

    def run_next_stage(self):
        self.stage += 1
        self.update_main_window()
        if self.sub_window_active:
            self.image_window.COUNT += 1
        else:
            self.sub_window()
        


    def sub_window(self):
        self.root = Tk()
        self.root.geometry("%dx%d+%d+%d" % (800, 600, 300, 300))
        self.root.title("Image Slideshow")
        self.image_window = DisplayImage(self.root, self.stage)
        self.image_window.next_image()
        self.sub_window_active = True
        self.root.mainloop()

    def func(self):
        if self.sub_window_active:
            if self.stage != self.image_window.curr_block:
                self.stage -= 1
            self.root.destroy()
            self.sub_window_active = False
        else:
            self.stage = 0
        self.update_main_window()
        #sys.exit(app.exec_())

    def get_phase(self):
        phase = self.combobox.currentText()
        return phase
    
    def onStageChange(self, text):
        if text == 'Neurofeedback':
            self.blocks = 1

            self.block2 = QtWidgets.QLabel()
            self.block2.setPixmap(self.image)
            self.block2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.block2.setFixedWidth(300)
            self.block2.setFixedHeight(50)

            self.block3 = QtWidgets.QLabel()
            self.block3.setPixmap(self.image)
            self.block3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.block3.setFixedWidth(300)
            self.block3.setFixedHeight(50)

            self.block4 = QtWidgets.QLabel()
            self.block4.setPixmap(self.image)
            self.block4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.block4.setFixedWidth(300)
            self.block4.setFixedHeight(50)

            self.block5 = QtWidgets.QLabel()
            self.block5.setPixmap(self.image)
            self.block5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.block5.setFixedWidth(300)
            self.block5.setFixedHeight(50)

            self.grid.addWidget(self.block2,4,1)
            self.grid.addWidget(self.block3,5,1)
            self.grid.addWidget(self.block4,6,1)
            self.grid.addWidget(self.block5,7,1)
        elif text == 'Post-Evaluation':
            if self.blocks == 1:
                self.block5.setParent(None)
                self.block4.setParent(None)
                self.block3.setParent(None)
                self.block2.setParent(None)
                self.blocks = 0
        elif text == 'Pre-Evaluation':
            if self.blocks == 1:
                self.block5.setParent(None)
                self.block4.setParent(None)
                self.block3.setParent(None)
                self.block2.setParent(None)
                self.blocks = 0

    def update_main_window(self):
        match self.stage:
            case 0:
                self.block.setPixmap(self.image)
            case 1:
                self.block.setPixmap(self.image1)
            case 2:
                self.block.setPixmap(self.image2)
            case 3:
                self.block.setPixmap(self.image3)
            case 4:
                self.block.setPixmap(self.image4)
            case 5:
                self.block.setPixmap(self.image5)
            case 6:
                self.block.setPixmap(self.image6)
            case 7:
                self.block.setPixmap(self.image7)
            case 8:
                self.block.setPixmap(self.image8)
        self.grid.addWidget(self.block, 3, 1)

    def add_patient_data(self):
        trial_data = self.line.text()
        with open('neruo.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Patient Name '])
            writer.writerow(trial_data)  # this technically iterates so will be wonky with single string till more info is captured
        print("Patient Data Collected")





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
