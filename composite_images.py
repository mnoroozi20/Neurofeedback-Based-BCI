import os
from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open("Images/MaleFace/10.jpg").convert("L") # load images and convert to greyscale
im2 = Image.open('Images/OutdoorScene/2.jpg').resize(im1.size).convert("L")

mask = Image.new("L", im1.size, 128)
# im = Image.composite(im1, im2, mask) # composite greyscale images using mask
im = Image.blend(im1, im2, 0.9)  # have neruofeedback change alpha 0.1 is closer to im1, 0.9 closer to im2
im.show()
