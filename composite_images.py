import os
from os import listdir
from PIL import Image, ImageDraw, ImageFilter
import random

# im1 = Image.open("Images/MaleFace/10.jpg").convert("L") # load images and convert to greyscale
# im2 = Image.open('Images/OutdoorScene/2.jpg').resize(im1.size).convert("L")

Block = '8'

# im = Image.blend(im1, im2, 0.9)  # have neruofeedback change alpha 0.1 is closer to im1, 0.9 closer to im2
# im.show()

composite_images = []

female_faces = []
folder_dir = os.getcwd() + "/Images/FemaleFace"
for image in os.listdir(folder_dir):
    female_faces.append(image)
random.shuffle(female_faces)

male_faces = []
folder_dir = os.getcwd() + "/Images/MaleFace"
for image in os.listdir(folder_dir):
    male_faces.append(image)
random.shuffle(male_faces)

outdoor_scenes = []
folder_dir = os.getcwd() + "/Images/OutdoorScene"
for image in os.listdir(folder_dir):
    outdoor_scenes.append(image)
random.shuffle(outdoor_scenes)

indoor_scenes = []
folder_dir = os.getcwd() + "/Images/IndoorScene"
for image in os.listdir(folder_dir):
    indoor_scenes.append(image)
random.shuffle(indoor_scenes)


fcount = 0
mcount = 0
ocount = 0
icount = 0
for i in range(41) :
    f = random.randint(0,1)
    match f:
        case 0:
            fcount = fcount + 1
            f_img = Image.open('Images/FemaleFace/' + female_faces[fcount]).convert('L')
        case 1:
            mcount = mcount + 1
            f_img = Image.open('Images/MaleFace/' + male_faces[mcount]).convert('L')
    s = random.randint(0,1)
    match s:
        case 0:
            ocount = ocount + 1
            s_img = Image.open('Images/OutdoorScene/' + outdoor_scenes[ocount]).convert('L')
        case 1:
            icount = icount + 1
            s_img = Image.open('Images/IndoorScene/' + indoor_scenes[icount]).convert('L')
    mask = Image.new("L", f_img.size, 128)
    im = Image.composite(f_img, s_img, mask) # composite greyscale images using mask
    im.save('Images/Composite_Images/Block' + Block + '/' + str(i) + '.jpg')

# create mask with image size, open two photos, blend the two images
