from PIL import Image
import os

count = 0;
for Sfiles in os.listdir('background'):
    im1 = Image.open(f'background/{Sfiles}')
    im1.save('backgroundJPEG/{}.jpeg'.format(count))
    count = count + 1