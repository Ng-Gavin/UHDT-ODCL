from secrets import choice
from PIL import Image, ImageFont, ImageDraw
import os
import random
import csv

import math
import numpy as np

#Function to take target shape and turn it into a numerical class for labelling
def shape_to_class(shape):
    switcher = {
        "circle": 0,
        "cross": 1,
        "heptagon": 2,
        "hexagon": 3,
        "octagon": 4,
        "pentagon": 5,
        "quartercircle": 6,
        "rectangle": 7,
        "semicircle": 8,
        "square": 9,
        "star": 10,
        "trapezoid": 11,
        "triangle": 12
    }
    return switcher.get(shape,"nothing")

#Define possible characteristics for targets
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (150, 150, 150)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Purple = (255, 0, 255)
Brown = (150, 105, 25)
Orange = (255, 150, 0)
colors = [White, Black, Gray, Red, Blue, Green, Yellow, Purple, Brown, Orange]
strcolors = ['White', 'Black', 'Gray', 'Red', 'Blue',
             'Green', 'Yellow', 'Purple', 'Brown', 'Orange']
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
    "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
shapes = []
backgrounds = []

shapeSize = 105
alphanumSize = 70
amount = 100

#Adds all filenames into respective lists
for Sfiles in os.listdir('Shape Plate'):
    if Sfiles.endswith('.png'):
        shapes.append(Sfiles)
for Bfiles in os.listdir('background'):
    if Bfiles.endswith('.png'):
        backgrounds.append(Bfiles)

#Set font and size of Alphanumeric
myfont = ImageFont.truetype('SourceSansPro-Black.ttf', alphanumSize)

for i in range(amount):
    background = random.choice(backgrounds)
    Background = Image.open(f'background/{background}')
    width, height = Background.size

    #Location of target in Q1
    xpos1 = random.randint(0, width/2-shapeSize)
    ypos1 = random.randint(0, height/2-shapeSize)
    #Location of target in Q2
    xpos2 = random.randint(width/2, width-shapeSize)
    ypos2 = random.randint(0, height/2-shapeSize)
    #Location of target in Q3
    xpos3 = random.randint(0, width/2-shapeSize)
    ypos3 = random.randint(height/2, height-shapeSize)
    #Location of target in Q4
    xpos4 = random.randint(width/2, width-shapeSize)
    ypos4 = random.randint(height/2, height-shapeSize)
    
    xpos = [xpos1,xpos2,xpos3,xpos4]
    ypos = [ypos1,ypos2,ypos3,ypos4]

    for tNum in range(4):
        print("Image#:",i," Target#:",tNum)

        #Selects random characteristics for targets
        letter = random.choice(letters)
        shape = random.choice(shapes)
        choice1 = random.randint(0, 9)
        choice2 = random.randint(0, 9)
        rotation = random.randint(0,360)
        while (choice1 == choice2):
            choice2 = random.randint(0, 9)
        shapeColor = colors[choice1]
        shapeColorSTR = strcolors[choice1]
        alphaColor = colors[choice2]
        alphaColorSTR = strcolors[choice2]

        Shape = Image.open(f'Shape Plate/{shape}')
        Sshape, fext = os.path.splitext(shape)
        
        im = Shape.convert('RGB')

        # "data" is a height x width x 4 numpy array
        data = np.array(im)
        
        shapeY, shapeX = np.where(np.all(data==[255,255,255],axis=2))

        top, bottom = shapeY[0], shapeY[-1]

        left, right = shapeX[0], shapeX[-1]
        
        ROI = data[top:bottom, left:right]

        ROIShape = Image.fromarray(ROI).convert('RGBA')

        data = np.array(ROIShape)

        red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability

        # Replace white with red... (leaves alpha values alone...)
        white_areas = (red == 255) & (blue == 255) & (green == 255)

        # Transpose back needed
        data[..., :-1][white_areas.T] = (shapeColor)

        ColoredShape = Image.fromarray(data)

        target = ImageDraw.Draw(ColoredShape)

        target.text((32, 8), letter, font=myfont, fill=alphaColor)

        RotatedShape = ColoredShape.rotate(rotation, expand=True, fillcolor=(0,0,0,0))

        targetX,targetY = RotatedShape.size

        Background.paste(RotatedShape, (xpos[tNum], ypos[tNum]), RotatedShape)

        file_name = str(i).zfill(5)

        Background.save('final/images/{}.jpg'.format(file_name))
    
        with open('final/labels/{}.txt'.format(file_name), 'a', encoding='utf-8') as f:
            f.write('{} {} {} {} {}\n'.format(shape_to_class(Sshape),
                                            (xpos[tNum]+(targetX/2))/width,
                                            (ypos[tNum]+(targetY/2))/height,
                                            (targetX+1)/width,
                                            (targetY+1)/height))