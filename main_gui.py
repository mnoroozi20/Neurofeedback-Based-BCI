import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        # self.setGeometry(50,50,1000,500)
        self.setWindowTitle("Window")
        self.setStyleSheet('background: #505050')
        self.stage = 3
        self.home()

    def home(self):
        grid = QtWidgets.QGridLayout()
        self.setLayout(grid)

        label1 = QtWidgets.QLabel('Patient:')
        label1.setFixedWidth(50)
        label1.setStyleSheet('font-size: 15px; ')

        self.line = QtWidgets.QLineEdit(self)
        self.line.setFixedWidth(200)
        # label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
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

        self.combobox = QtWidgets.QComboBox(self)
        self.combobox.addItem('Pre-Evaluation')
        self.combobox.addItem('Neurofeedback')
        self.combobox.addItem('Post-Evaluation')
        self.combobox.setFixedWidth(100)
        self.combobox.setStyleSheet('background: #FFFFFF; margin-left: 1px; margin-right: 1px')

        label3 = QtWidgets.QLabel('Stage:')
        label3.setFixedWidth(50)
        label3.setStyleSheet('font-size: 15px')

        self.image_button = QPushButton(self)
        self.image_button.setFixedWidth(120)
        self.image_button.setText('Image Window')
        self.image_button.setStyleSheet('font-size:15px; background: #DF6D22;')

        image = QtGui.QPixmap("Assets/BlockLoad" + str(self.stage) + "_5.png").scaled(175, 175, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        block = QtWidgets.QLabel()
        block.setPixmap(image)
        block.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        block.setFixedWidth(175)

        grid.addWidget(label1, 0, 0)
        grid.addWidget(self.line, 0, 1)
        grid.addWidget(start_btn, 0, 2)
        grid.addWidget(stop_btn, 0, 3)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.combobox, 1, 1)
        grid.addWidget(label3, 2, 0)
        grid.addWidget(block, 2, 1)
        grid.addWidget(self.image_button, 3, 1)
        self.show()

        # Sub Window
        self.sub_window = SubWindow()
        self.image_button.clicked.connect(self.sub_window.show)

    def func(self):
        print(self.line.text())

    def get_phase(self):
        phase = self.combobox.currentText()
        return phase


class SubWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QGridLayout(self)
        self.resize(500, 500)
        self.setWindowTitle("Image Window")
        self.setStyleSheet('background: #505050')

        self.label = QtWidgets.QLabel()
        layout.addWidget(self.label, 0, 0, 1, 2)
        self.label.setMinimumSize(200, 200)
        # the label alignment property is always maintained even when the contents
        # change, so there is no need to set it each time
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.loadImageButton = QtWidgets.QPushButton('Load image')
        layout.addWidget(self.loadImageButton, 1, 0)

        self.nextImageButton = QtWidgets.QPushButton('Next image')
        layout.addWidget(self.nextImageButton)

        self.loadImageButton.clicked.connect(self.loadImage)
        self.nextImageButton.clicked.connect(self.nextImage)

        self.dirIterator = None
        self.fileList = []

    def loadImage(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg)')
        if filename:
            pixmap = QtGui.QPixmap(filename).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.label.setPixmap(pixmap)
            dirpath = os.path.dirname(filename)
            self.fileList = []
            for f in os.listdir(dirpath):
                fpath = os.path.join(dirpath, f)
                if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
                    self.fileList.append(fpath)
            self.fileList.sort()
            self.dirIterator = iter(self.fileList)
            while True:
                # cycle through the iterator until the current file is found
                if next(self.dirIterator) == filename:
                    break

    def nextImage(self):
        # ensure that the file list has not been cleared due to missing files
        if self.fileList:
            try:
                filename = next(self.dirIterator)
                pixmap = QtGui.QPixmap(filename).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    # the file is not a valid image, remove it from the list
                    # and try to load the next one
                    self.fileList.remove(filename)
                    self.nextImage()
                else:
                    self.label.setPixmap(pixmap)
            except:
                # the iterator has finished, restart it
                self.dirIterator = iter(self.fileList)
                self.nextImage()
        else:
            # no file list found, load an image
            self.loadImage()


    # def __init__(self):
    #     super(SubWindow, self).__init__()
    #     self.resize(400, 300)
    #     self.setWindowTitle("SubWindow")
    #     self.setStyleSheet('background: #505050')
    #     self.stage = 3
    #     self.main()
    #
    # def main(self):
    #     grid = QtWidgets.QGridLayout()
    #     self.setLayout(grid)
    #
    #     start_btn = QtWidgets.QPushButton('Start', self)
    #     start_btn.setFixedWidth(75)
    #     start_btn.setStyleSheet('background: #228C22')
    #
    #     close_btn = QtWidgets.QPushButton('Close', self)
    #     close_btn.clicked.connect(lambda: self.close())
    #     close_btn.setFixedWidth(75)
    #     close_btn.setStyleSheet('background: #B80F0A')
    #
    #     grid.addWidget(start_btn, 0, 1)
    #     grid.addWidget(close_btn, 0, 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
