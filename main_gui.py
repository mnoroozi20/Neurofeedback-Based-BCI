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
        self.setStyleSheet('background: #505050')
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        # Sub Window
        self.sub_window = SubWindow()
        self.stage = 3
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
        self.start_btn.clicked.connect(self.image_window)

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
        self.block.setPixmap(self.image3)
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

    def image_window(self):
        root = Tk()
        root.geometry("%dx%d+%d+%d" % (800, 600, 300, 300))
        root.title("Image Slideshow")
        image_window = DisplayImage(root)
        image_window.next_image()
        root.mainloop()

    def func(self):
        sys.exit(app.exec_())

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

    def add_patient_data(self):
        trial_data = self.line.text()
        with open('neruo.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Patient Name '])
            writer.writerow(trial_data)  # this technically iterates so will be wonky with single string till more info is captured
        print("Patient Data Collected")


class SubWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QGridLayout(self)
        self.resize(500, 500)
        self.setWindowTitle("Image Window")
        self.setStyleSheet('background: #505050')

        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.label.setMinimumSize(200, 200)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.loadImageButton = QtWidgets.QPushButton('Load image')
        self.loadImageButton.setStyleSheet("background: #FFFFFF")
        self.layout.addWidget(self.loadImageButton, 1, 0)

        self.nextImageButton = QtWidgets.QPushButton('Next image')
        self.nextImageButton.setStyleSheet("background: #FFFFFF")
        self.layout.addWidget(self.nextImageButton)

        self.loadImageButton.clicked.connect(self.load_image)
        self.nextImageButton.clicked.connect(self.next_image)

        self.image_bank = iter(["Images/2.jpg", "Images/3.jpg", "Images/4.jpg", "Images/5.jpg", ])
        self.count = 2

    def load_image(self):

        pixmap = QPixmap('Images/1.jpg').scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.show()

    def next_image(self):
        current_pixmap = QPixmap(f"Images/{self.count}.jpg").scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(current_pixmap)
        self.count += 1
        if current_pixmap.isNull():
            self.close()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
