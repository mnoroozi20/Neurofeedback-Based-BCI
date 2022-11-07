import UnicornPy
import numpy as np
import pandas as pd
import pygame
import random
import gui
import sys


# arduino-python code

class Arduino:
    def __init__(self, initial_data, sample_number, sample_rate, states, arduinoData, arduinoData2):
        self.sample_rate = sample_rate
        self.sample = sample_number
        self.data = initial_data
        self.current_state = 3
        self.states = states
        self.arduinoData = arduinoData
        self.arduinoData2 = arduinoData2
        self.img_size = (250, 100)
