import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1000,500)
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

        self.line = QtWidgets.QLineEdit(self)
        self.line.setFixedWidth(200)
        # label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.line.setStyleSheet('background: #EEEEEE; margin-right: 20px')

        self.start_btn = QtWidgets.QPushButton('Start', self)
        self.start_btn.setFixedWidth(75)
        self.start_btn.setStyleSheet('background: #228C22')
        self.start_btn.clicked.connect(self.sub_window.show)

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
        self.grid.addWidget(self.label2, 1, 0)
        self.grid.addWidget(self.combobox, 1, 1)
        self.grid.addWidget(self.label3, 2, 0)
        self.grid.addWidget(self.block, 2, 1)
        self.show()

        

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

            self.grid.addWidget(self.block2,3,1)
            self.grid.addWidget(self.block3,4,1)
            self.grid.addWidget(self.block4,5,1)
            self.grid.addWidget(self.block5,6,1)
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
        # the label alignment property is always maintained even when the contents
        # change, so there is no need to set it each time
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.loadImageButton = QtWidgets.QPushButton('Load image')
        self.loadImageButton.setStyleSheet("background: #FFFFFF")
        self.layout.addWidget(self.loadImageButton, 1, 0)

        self.nextImageButton = QtWidgets.QPushButton('Next image')
        self.nextImageButton.setStyleSheet("background: #FFFFFF")
        self.layout.addWidget(self.nextImageButton)

        self.loadImageButton.clicked.connect(self.load_image)
        self.nextImageButton.clicked.connect(self.next_image)

        self.dirIterator = None
        self.fileList = []

        self.count = 2

    # def load_image(self):
    #     filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg)')
    #     if filename:
    #         pixmap = QtGui.QPixmap(filename).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
    #         if pixmap.isNull():
    #             return
    #         self.label.setPixmap(pixmap)
    #         dirpath = os.path.dirname(filename)
    #         self.fileList = []
    #         for f in os.listdir(dirpath):
    #             fpath = os.path.join(dirpath, f)
    #             if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
    #                 self.fileList.append(fpath)
    #         self.fileList.sort()
    #         self.dirIterator = iter(self.fileList)
    #         while True:
    #             # cycle through the iterator until the current file is found
    #             if next(self.dirIterator) == filename:
    #                 break
    #
    # def next_image(self):
    #     # ensure that the file list has not been cleared due to missing files
    #     if self.fileList:
    #         try:
    #             filename = next(self.dirIterator)
    #             pixmap = QtGui.QPixmap(filename).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
    #             if pixmap.isNull():
    #                 # the file is not a valid image, remove it from the list
    #                 # and try to load the next one
    #                 self.fileList.remove(filename)
    #                 self.nextImage()
    #             else:
    #                 self.label.setPixmap(pixmap)
    #         except:
    #             # the iterator has finished, restart it
    #             self.dirIterator = iter(self.fileList)
    #             self.nextImage()
    #     else:
    #         # no file list found, load an image
    #         self.loadImage()

    def load_image(self):

        pixmap = QPixmap('Images/1.jpg')
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.show()

        # Connect button to image updating

    def next_image(self):
        # pic = QtGui.QLabel(self)
        # pic.setGeometry(100, 10, 800, 800)
        image_bank = ["Images/2.jpg", "Images/3.jpg", "Images/4.jpg", "Images/5.jpg", ]

        self.label.setPixmap(QtGui.QPixmap(f"Images/{self.count}.jpg"))
        self.count += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
