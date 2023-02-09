import os
from os import listdir
from PIL import Image, ImageDraw, ImageFilter
import random
import pandas as pd

# im1 = Image.open("Images/MaleFace/10.jpg").convert("L") # load images and convert to greyscale
# im2 = Image.open('Images/OutdoorScene/2.jpg').resize(im1.size).convert("L")

Block = '8'
#45 - 5 ratio

# im = Image.blend(im1, im2, 0.9)  # have neruofeedback change alpha 0.1 is closer to im1, 0.9 closer to im2
# im.show()


female_faces = []
folder_dir = os.getcwd() + "/Images/FemaleFace"
for image in os.listdir(folder_dir):
    female_faces.append(image)

male_faces = []
folder_dir = os.getcwd() + "/Images/MaleFace"
for image in os.listdir(folder_dir):
    male_faces.append(image)

outdoor_scenes = []
folder_dir = os.getcwd() + "/Images/OutdoorScene"
for image in os.listdir(folder_dir):
    outdoor_scenes.append(image)

indoor_scenes = []
folder_dir = os.getcwd() + "/Images/IndoorScene"
for image in os.listdir(folder_dir):
    indoor_scenes.append(image)

#2 female face blocks
for n in range(2):
    random.shuffle(female_faces)
    random.shuffle(male_faces)
    random.shuffle(outdoor_scenes)
    random.shuffle(indoor_scenes)
    Block = str(n+1)
    instructions = []
    faces = []
    scenes = []
    fcount = 0
    mcount = 0
    ocount = 0
    icount = 0
    composite_images = []
    for i in range(40) :
        instructions.append('F')
        if fcount < 36:
            fcount = fcount + 1
            faces.append('F')
            f_img = Image.open('Images/FemaleFace/' + female_faces[fcount]).convert('L')
        else:
            mcount = mcount + 1
            faces.append('M')
            f_img = Image.open('Images/MaleFace/' + male_faces[mcount]).convert('L')
        s = random.randint(0,1)
        match s:
            case 0:
                ocount = ocount + 1
                scenes.append('O')
                s_img = Image.open('Images/OutdoorScene/' + outdoor_scenes[ocount]).convert('L')
            case 1:
                icount = icount + 1
                scenes.append('I')
                s_img = Image.open('Images/IndoorScene/' + indoor_scenes[icount]).convert('L')
        mask = Image.new("L", f_img.size, 128)
        im = Image.composite(f_img, s_img, mask) # composite greyscale images using mask
        composite_images.append(im)
    temp = list(zip(composite_images, faces, scenes))
    random.shuffle(temp)
    s_composite_images, s_faces, s_scenes = zip(*temp)
    s_composite_images, s_faces, s_scenes = list(s_composite_images), list(s_faces), list(s_scenes)
    for i in range(len(s_composite_images)) :
            s_composite_images[i].save('Images/Composite_Images/Block' + Block + '/' + str(i) + '.jpg')
    data = {'Instructions': instructions, 'Face': s_faces, 'Scene': s_scenes}
    image_key = pd.DataFrame(data)
    image_key.to_csv('Images/Composite_Images_key/Block' + Block + '_key.csv')
    del instructions
    del faces
    del scenes
    del composite_images
    del s_faces
    del s_scenes
    del s_composite_images
    del data
    del image_key
    del temp





#2 male face blocks
for n in range(2):
    random.shuffle(female_faces)
    random.shuffle(male_faces)
    random.shuffle(outdoor_scenes)
    random.shuffle(indoor_scenes)
    Block = str(n+3)
    instructions = []
    faces = []
    scenes = []
    fcount = 0
    mcount = 0
    ocount = 0
    icount = 0
    composite_images = []
    for i in range(40) :
        instructions.append('M')
        if mcount < 36:
            mcount = mcount + 1
            faces.append('M')
            f_img = Image.open('Images/MaleFace/' + male_faces[mcount]).convert('L')
        else:
            fcount = fcount + 1
            faces.append('F')
            f_img = Image.open('Images/FemaleFace/' + female_faces[fcount]).convert('L')
        s = random.randint(0,1)
        match s:
            case 0:
                ocount = ocount + 1
                scenes.append('O')
                s_img = Image.open('Images/OutdoorScene/' + outdoor_scenes[ocount]).convert('L')
            case 1:
                icount = icount + 1
                scenes.append('I')
                s_img = Image.open('Images/IndoorScene/' + indoor_scenes[icount]).convert('L')
        mask = Image.new("L", f_img.size, 128)
        im = Image.composite(f_img, s_img, mask) # composite greyscale images using mask
        composite_images.append(im)
    temp = list(zip(composite_images, faces, scenes))
    random.shuffle(temp)
    s_composite_images, s_faces, s_scenes = zip(*temp)
    s_composite_images, s_faces, s_scenes = list(s_composite_images), list(s_faces), list(s_scenes)
    for i in range(len(s_composite_images)) :
            s_composite_images[i].save('Images/Composite_Images/Block' + Block + '/' + str(i) + '.jpg')
    data = {'Instructions': instructions, 'Face': s_faces, 'Scene': s_scenes}
    image_key = pd.DataFrame(data)
    image_key.to_csv('Images/Composite_Images_key/Block' + Block + '_key.csv')
    del instructions
    del faces
    del scenes
    del composite_images
    del s_faces
    del s_scenes
    del s_composite_images
    del data
    del image_key
    del temp





#2 Outdoor blocks
for n in range(2):
    random.shuffle(female_faces)
    random.shuffle(male_faces)
    random.shuffle(outdoor_scenes)
    random.shuffle(indoor_scenes)
    Block = str(n+5)
    instructions = []
    faces = []
    scenes = []
    fcount = 0
    mcount = 0
    ocount = 0
    icount = 0
    composite_images = []
    for i in range(40) :
        instructions.append('O')
        if ocount < 36:
            ocount = ocount + 1
            scenes.append('O')
            s_img = Image.open('Images/OutdoorScene/' + outdoor_scenes[ocount]).convert('L')
        else:
            icount = icount + 1
            scenes.append('I')
            s_img = Image.open('Images/IndoorScene/' + indoor_scenes[icount]).convert('L')
        s = random.randint(0,1)
        match s:
            case 0:
                fcount = fcount + 1
                faces.append('F')
                f_img = Image.open('Images/FemaleFace/' + female_faces[fcount]).convert('L')
            case 1:
                mcount = mcount + 1
                faces.append('M')
                f_img = Image.open('Images/MaleFace/' + male_faces[mcount]).convert('L')
        mask = Image.new("L", f_img.size, 128)
        im = Image.composite(f_img, s_img, mask) # composite greyscale images using mask
        composite_images.append(im)
    temp = list(zip(composite_images, faces, scenes))
    random.shuffle(temp)
    s_composite_images, s_faces, s_scenes = zip(*temp)
    s_composite_images, s_faces, s_scenes = list(s_composite_images), list(s_faces), list(s_scenes)
    for i in range(len(s_composite_images)) :
            s_composite_images[i].save('Images/Composite_Images/Block' + Block + '/' + str(i) + '.jpg')
    data = {'Instructions': instructions, 'Face': s_faces, 'Scene': s_scenes}
    image_key = pd.DataFrame(data)
    image_key.to_csv('Images/Composite_Images_key/Block' + Block + '_key.csv')
    del instructions
    del faces
    del scenes
    del composite_images
    del s_faces
    del s_scenes
    del s_composite_images
    del data
    del image_key
    del temp




#2 Indoor face blocks
for n in range(2):
    random.shuffle(female_faces)
    random.shuffle(male_faces)
    random.shuffle(outdoor_scenes)
    random.shuffle(indoor_scenes)
    Block = str(n+7)
    instructions = []
    faces = []
    scenes = []
    fcount = 0
    mcount = 0
    ocount = 0
    icount = 0
    composite_images = []
    for i in range(40) :
        instructions.append('I')
        if icount < 36:
            icount = icount + 1
            scenes.append('I')
            s_img = Image.open('Images/IndoorScene/' + indoor_scenes[icount]).convert('L')
        else:
            ocount = ocount + 1
            scenes.append('O')
            s_img = Image.open('Images/OutdoorScene/' + outdoor_scenes[ocount]).convert('L')
        s = random.randint(0,1)
        match s:
            case 0:
                fcount = fcount + 1
                faces.append('F')
                f_img = Image.open('Images/FemaleFace/' + female_faces[fcount]).convert('L')
            case 1:
                mcount = mcount + 1
                faces.append('M')
                f_img = Image.open('Images/MaleFace/' + male_faces[mcount]).convert('L')
        mask = Image.new("L", f_img.size, 128)
        im = Image.composite(f_img, s_img, mask) # composite greyscale images using mask
        composite_images.append(im)
    temp = list(zip(composite_images, faces, scenes))
    random.shuffle(temp)
    s_composite_images, s_faces, s_scenes = zip(*temp)
    s_composite_images, s_faces, s_scenes = list(s_composite_images), list(s_faces), list(s_scenes)
    for i in range(len(s_composite_images)) :
            s_composite_images[i].save('Images/Composite_Images/Block' + Block + '/' + str(i) + '.jpg')
    data = {'Instructions': instructions, 'Face': s_faces, 'Scene': s_scenes}
    image_key = pd.DataFrame(data)
    image_key.to_csv('Images/Composite_Images_key/Block' + Block + '_key.csv')
    del instructions
    del faces
    del scenes
    del composite_images
    del s_faces
    del s_scenes
    del s_composite_images
    del data
    del image_key
    del temp