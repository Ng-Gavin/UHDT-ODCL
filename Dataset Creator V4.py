from secrets import choice
from PIL import Image, ImageFont, ImageDraw
import os
import random

import math
import numpy as np

# calulate: letters * shapes * backgrounds
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
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
shapes = []
backgrounds = []

amount = 2

#for Lfiles in os.listdir('Letter Plate'):  # looks throught the file
#    if Lfiles.endswith('.png'):  # only looks for png images
#        letters.append(Image.open(f'Letter Plate/{Lfiles}'))

for Sfiles in os.listdir('Shape Plate'):
    if Sfiles.endswith('.png'):
        shapes.append(Sfiles)

for Bfiles in os.listdir('background'):
    if Bfiles.endswith('.png'):
        backgrounds.append(Bfiles)

myfont = ImageFont.truetype('SourceSansPro-Black.ttf',90)

while (amount > 0):
    letter = random.choice(letters)
    shape = random.choice(shapes)
    background = random.choice(backgrounds)
    choice1 = random.randint(0, 9)
    choice2 = random.randint(0, 9)
    while (choice1 == choice2):
        choice2 = random.randint(0, 9)
    shapeColor = colors[choice1]
    shapeColorSTR = strcolors[choice1]
    alphaColor = colors[choice2]
    alphaColorSTR = strcolors[choice2]


    Shape = Image.open(f'Shape Plate/{Sfiles}')
    Sfn, fext = os.path.splitext(Sfiles)
    Sshape, Scolor = Sfn.split('-')

    im = Shape.convert('RGBA')

    # "data" is a height x width x 4 numpy array
    data = np.array(im)
    red, green, blue, alpha = data.T  # Temporarily unpack the bands for readability

    # Replace white with red... (leaves alpha values alone...)
    white_areas = (red == 255) & (blue == 255) & (green == 255)

    # Transpose back needed
    data[..., :-1][white_areas.T] = (shapeColor)

    ColoredShape = Image.fromarray(data)

    Background = Image.open(f'background/{Bfiles}')
    
    background, fext = os.path.splitext(Bfiles)
    width, height = Background.size  # will get the size of the background img
    
    ShapeResize = ColoredShape.resize((int(105), int(105)))
    Swidth, Sheight = ShapeResize.size

    target = ImageDraw.Draw(ShapeResize)

    target.text((41,20), letter, font = myfont, fill = alphaColor)

    rotated = ShapeResize.rotate(90)

    Background.paste(rotated, (165, 165), rotated)

    print(f'{alphaColorSTR} {letter} {Scolor} {Sshape} {background}')
    Background.show()
    Background.save('final/{} {} {} {} {}.jpg'.format(alphaColorSTR, letter, shapeColorSTR, Sshape, background))
    amount = amount - 1
3