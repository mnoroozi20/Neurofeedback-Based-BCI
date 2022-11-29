import os
from os import listdir
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
from PIL import Image, ImageDraw, ImageFilter


class DisplayImage:

    def __init__(self, master):
        self.master = master
        self.image_arr = []
        self.COUNT = 0

        self.folder_dir = "C:/Users/tnlab/PycharmProjects/Neurofeedback-Based-BCI/Images/IndoorScene"
        self.TIME_BETWEEN = 1000
        self.CURRENT_FOLDER = "IndoorScene"

        for images in os.listdir(self.folder_dir):
            if images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg"):
                # display
                self.image_arr.append(images)

        self.my_canvas = Canvas(master, width=800, height=600, highlightthickness=0)
        self.my_canvas.pack()

        im = Image.open(f"Images/{self.CURRENT_FOLDER}/{self.image_arr[self.COUNT]}")
        resized = im.resize((800, 600), Image.Resampling.LANCZOS)
        ph = ImageTk.PhotoImage(resized)

        self.label = Label(self.my_canvas, image=ph, width=800, height=600)
        self.label.config(anchor=CENTER)
        self.label.pack()

    def next_image(self):

        if self.COUNT >= 50:  # count to be determined based off of how many images in folder
            next_img = Image.open(f"Images/please-wait.png")
            next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(next_img_resized)
            self.label.config(image=photo_img)
            self.label.image = photo_img

        else:
            next_img = Image.open(f"Images/{self.CURRENT_FOLDER}/{self.image_arr[self.COUNT]}")
            next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(next_img_resized)
            self.label.config(image=photo_img)
            self.label.image = photo_img
            self.COUNT += 1

        self.master.after(self.TIME_BETWEEN, self.next_image)


if __name__ == "__main__":
    root = Tk()
    root.geometry("%dx%d+%d+%d" % (800, 600, 300, 300))
    root.title("Image Slideshow")
    main_window = DisplayImage(root)
    main_window.next_image()
    root.mainloop()