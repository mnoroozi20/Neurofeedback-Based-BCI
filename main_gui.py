import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import csv
import time
from os import listdir
from image_display import *
import numpy as np


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1000, 500)
        self.setWindowTitle("Main Window")
        self.setStyleSheet('background: #707070')
        self.grid = QtWidgets.QGridLayout()
        self.setLayout(self.grid)
        self.sub_window_active = False
        self.patient_progress = ['', '0', '0', '0','1']
        self.stage = 0
        self.pre_stage = 0
        self.neuro_stage = 0
        self.post_stage = 0
        self.block = None
        self.patient_list = []
        self.patient_index = 0
        with open('NF_Patient_Progress.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.patient_list.append(row)
        self.create_home()

    def create_home(self):
        self.blocks = 0

        patient_label = QtWidgets.QLabel('Patient:')
        patient_label.setFixedWidth(50)
        patient_label.setStyleSheet('font-size: 15px; ')

        self.patient_btn = QtWidgets.QPushButton('Add Patient Data', self)
        self.patient_btn.setFixedWidth(100)
        self.patient_btn.setStyleSheet('background: #1634EF')
        self.patient_btn.clicked.connect(self.add_patient_data)

        self.patient_data_entry = QtWidgets.QLineEdit(self)
        self.patient_data_entry.setFixedWidth(200)
        # patient_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.patient_data_entry.setStyleSheet('background: #EEEEEE; margin-right: 20px')

        self.start_btn = QtWidgets.QPushButton('Start', self)
        self.start_btn.setFixedWidth(75)
        self.start_btn.setStyleSheet('background: #228C22')
        self.start_btn.clicked.connect(self.run_next_stage)

        self.stop_btn = QtWidgets.QPushButton('Stop', self)
        self.stop_btn.setFixedWidth(75)
        self.stop_btn.setStyleSheet('background: #B80F0A')
        self.stop_btn.clicked.connect(self.stop_trial_func)

        self.phase_label = QtWidgets.QLabel('Phase:')
        self.phase_label.setFixedWidth(50)
        self.phase_label.setStyleSheet('font-size: 15px')

        self.phase_combobox = QtWidgets.QComboBox(self)
        self.phase_combobox.addItem('Pre-Evaluation')
        self.phase_combobox.addItem('Neurofeedback')
        self.phase_combobox.addItem('Post-Evaluation')
        self.phase_combobox.setFixedWidth(100)
        self.phase_combobox.setStyleSheet('background: #FFFFFF; margin-left: 1px; margin-right: 1px')
        self.phase_combobox.activated[str].connect(self.onStageChange)

        self.stage_label = QtWidgets.QLabel('Stage:')
        self.stage_label.setFixedWidth(50)
        self.stage_label.setStyleSheet('font-size: 15px')

        self.image = QtGui.QPixmap("Asssets/BlockLoad0_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image1 = QtGui.QPixmap("Asssets/BlockLoad1_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image2 = QtGui.QPixmap("Asssets/BlockLoad2_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image3 = QtGui.QPixmap("Asssets/BlockLoad3_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image4 = QtGui.QPixmap("Asssets/BlockLoad4_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image5 = QtGui.QPixmap("Asssets/BlockLoad5_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image6 = QtGui.QPixmap("Asssets/BlockLoad6_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image7 = QtGui.QPixmap("Asssets/BlockLoad7_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.image8 = QtGui.QPixmap("Asssets/BlockLoad8_8.png").scaled(300, 300, QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        self.block_num_img = QtWidgets.QLabel()
        self.block_num_img.setPixmap(self.image)
        self.block_num_img.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.block_num_img.setFixedWidth(300)
        self.block_num_img.setFixedHeight(50)

        self.grid.addWidget(patient_label, 0, 0)
        self.grid.addWidget(self.patient_data_entry, 0, 1)
        self.grid.addWidget(self.start_btn, 0, 2)
        self.grid.addWidget(self.stop_btn, 0, 3)
        self.grid.addWidget(self.patient_btn, 1, 1)
        self.grid.addWidget(self.phase_label, 2, 0)
        self.grid.addWidget(self.phase_combobox, 2, 1)
        self.grid.addWidget(self.stage_label, 3, 0)
        self.grid.addWidget(self.block_num_img, 3, 1)
        self.show()

    def run_next_stage(self):
        if self.sub_window_active:
            self.image_window.pause = False
        else:
            self.add_patient_data()
            self.sub_window()

        self.stage += 1
        if self.phase_combobox.currentText() == 'Pre-Evaluation':
            if self.stage > 8:
                self.stage = 1
            self.pre_stage = self.stage
            self.patient_progress[1] = str(self.stage)
        elif self.phase_combobox.currentText() == 'Post-Evaluation':
            if self.stage > 8:
                self.stage = 1
            self.pre_stage = self.stage
            self.patient_progress[3] = str(self.stage)
        self.update_patient_data()
        self.update_main_window()

    def sub_window(self):
        self.root = Tk()
        self.root.geometry("%dx%d+%d+%d" % (800, 600, 300, 300))
        self.root.title("Image Slideshow")
        self.image_window = DisplayImage(self.root, self.stage)
        self.block_sequence = self.image_window.randomized_blocks
        self.seq = " ".join(str(x) for x in self.block_sequence)
        print(self.seq)
        self.image_window.next_image()
        self.sub_window_active = True
        self.root.mainloop()

    def stop_trial_func(self):
        if self.sub_window_active:
            if self.stage < self.image_window.curr_block:
                self.stage -= 1
                self.update_patient_data()
            self.root.destroy()
            self.sub_window_active = False
        else:
            self.patient_data_entry.clear()
            self.patient_progress = ['', '0', '0', '0']
            self.stage = 0
        self.update_main_window()
        # sys.exit(app.exec_())

    def get_phase(self):
        phase = self.phase_combobox.currentText()
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

            self.grid.addWidget(self.block2, 4, 1)
            self.grid.addWidget(self.block3, 5, 1)
            self.grid.addWidget(self.block4, 6, 1)
            self.grid.addWidget(self.block5, 7, 1)
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
        self.update_main_window()

    def update_main_window(self):
        # match self.phase_combobox.currentText():
        #     case 'Pre-Evaluation':
        #         self.stage = int(self.patient_progress[1])
        #     case 'Neurofeedback':
        #         self.stage = int(self.patient_progress[2])
        #     case 'Post-Evaluation':
        #         self.stage = int(self.patient_progress[3])

        if self.phase_combobox.currentText() == 'Pre-Evaluation':
            self.stage = int(self.patient_progress[1])
        elif self.phase_combobox.currentText() == 'Neurofeedback':
            self.stage = int(self.patient_progress[2])
        elif self.phase_combobox.currentText() == 'Post-Evaluation':
            self.stage = int(self.patient_progress[3])

        if self.phase_combobox.currentText() == 'Neurofeedback':
            self.stage = self.patient_progress[2]
        else:
            if self.stage == 0:
                self.block_num_img.setPixmap(self.image)
            elif self.stage == 1:
                self.block_num_img.setPixmap(self.image1)
            elif self.stage == 2:
                self.block_num_img.setPixmap(self.image2)
            elif self.stage == 3:
                self.block_num_img.setPixmap(self.image3)
            elif self.stage == 4:
                self.block_num_img.setPixmap(self.image4)
            elif self.stage == 5:
                self.block_num_img.setPixmap(self.image5)
            elif self.stage == 6:
                self.block_num_img.setPixmap(self.image6)
            elif self.stage == 7:
                self.block_num_img.setPixmap(self.image7)
            elif self.stage == 8:
                self.block_num_img.setPixmap(self.image8)

            # match self.stage:
            #     case 0:
            #         self.block_num_img.setPixmap(self.image)
            #     case 1:
            #         self.block_num_img.setPixmap(self.image1)
            #     case 2:
            #         self.block_num_img.setPixmap(self.image2)
            #     case 3:
            #         self.block_num_img.setPixmap(self.image3)
            #     case 4:
            #         self.block_num_img.setPixmap(self.image4)
            #     case 5:
            #         self.block_num_img.setPixmap(self.image5)
            #     case 6:
            #         self.block_num_img.setPixmap(self.image6)
            #     case 7:
            #         self.block_num_img.setPixmap(self.image7)
            #     case 8:
            #         self.block_num_img.setPixmap(self.image8)
            self.grid.addWidget(self.block_num_img, 3, 1)

    def add_patient_data(self):
        patient_name = self.patient_data_entry.text()
        self.patient_progress[0] = patient_name
        i = 0
        for row in self.patient_list:
            if row[0] == self.patient_progress[0]:
                self.patient_index = i
                self.patient_progress = row
                self.pre_stage = int(self.patient_progress[1])
                self.neuro_stage = int(self.patient_progress[2])
                self.post_stage = int(self.patient_progress[3])
                self.update_main_window()
                return
            i += 1
        with open('NF_Patient_Progress.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                self.patient_progress)  # this technically iterates so will be wonky with single string till more info is captured
            file.close()
        self.patient_list.append(self.patient_progress)
        self.patient_index = len(self.patient_list) - 1
        self.update_main_window()
        print('Patient Data Added')
        print(self.patient_progress)

    def update_patient_data(self):
        self.patient_progress[4] = self.seq
        self.patient_list[self.patient_index] = self.patient_progress
        with open('NF_Patient_Progress.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in self.patient_list:
                writer.writerow(row)
            file.close()
        self.update_main_window()
        print('Patient Data Updated')
        print(self.patient_progress)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
