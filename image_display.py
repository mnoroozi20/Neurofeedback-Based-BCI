import os
from os import listdir
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
from PIL import Image, ImageDraw, ImageFilter


class DisplayImage:

    def __init__(self, master, stage):
        self.master = master
        self.image_arr = []
        self.curr_block = stage
        self.COUNT = stage * 40
        self.pause = True
        self.folder_dir = os.getcwd() + "/Images/Composite_Images"
        self.TIME_BETWEEN = 1000
        for i in range(8):
            self.CURRENT_FOLDER = "/Block" + str(i+1)
            for images in range(40):
                img = Image.open(f"Images/Composite_Images/Block{i+1}/{images+1}.jpg")
                self.image_arr.append(img)
        self.my_canvas = Canvas(self.master, width=800, height=600, highlightthickness=0)
        self.my_canvas.pack()
        im = self.image_arr[0]
        resized = im.resize((800, 600), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)
        self.label = Label(self.my_canvas, image=ph, width=800, height=600)
        self.label.config(anchor=CENTER)
        self.label.pack()


    def next_image(self):

        if self.pause:  # count to be determined based off of how many images in folder
            next_img = Image.open(f"Images/please-wait.png")
            next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(next_img_resized)
            self.label.config(image=photo_img)
            self.label.image = photo_img

        else:
            next_img = self.image_arr[self.COUNT]
            next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(next_img_resized)
            self.label.config(image=photo_img)
            self.label.image = photo_img
            self.COUNT += 1
            if self.COUNT%10 == 0:
                self.pause = True
                self.curr_block += 1
                

        self.master.after(self.TIME_BETWEEN, self.next_image)


if __name__ == "__main__":
    root = Tk()
    root.geometry("%dx%d+%d+%d" % (800, 600, 300, 300))
    root.title("Image Slideshow")
    main_window = DisplayImage(root)
    main_window.next_image()
    root.mainloop()
