import os
from os import listdir
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x600")
root.title('Image Slideshow')

# get the path or directory,  could update this folder dir automatically to get correct images on certain phase
folder_dir = "C:/Users/benja/PycharmProjects/Neurofeedback-Based-BCI/Images"
image_arr = []

TIME_BETWEEN = 1000
COUNT = 0

for images in os.listdir(folder_dir):
    if images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg"):
        # display
        image_arr.append(images)


my_canvas = Canvas(root, width=800, height=600, highlightthickness=0)
my_canvas.pack()


im = Image.open(f"Images/{image_arr[COUNT]}")
resized = im.resize((800, 600), Image.Resampling.LANCZOS)
ph = ImageTk.PhotoImage(resized)

label = Label(my_canvas, image=ph, width=800, height=600)
label.config(anchor=CENTER)
label.pack()


def next_image():
    global COUNT
    if COUNT == 10:
        next_img = Image.open(f"Images/{image_arr[COUNT]}")
        next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(next_img_resized)
        label.config(image=photo_img)
        label.image = photo_img

    else:
        next_img = Image.open(f"Images/{image_arr[COUNT]}")
        next_img_resized = next_img.resize((800, 600), Image.Resampling.LANCZOS)
        photo_img = ImageTk.PhotoImage(next_img_resized)
        label.config(image=photo_img)
        label.image = photo_img
        COUNT += 1

    root.after(TIME_BETWEEN, next_image)


next_image()
mainloop()
