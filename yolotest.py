import cv2
import torch
import os
from PIL import Image

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt')

images = []

#dir = 'datasets/dataset3/test/images/'
dir = 'background/'
imgs = [dir + f for f in os.listdir(dir)]#
# Images
#for f in os.listdir('datasets/dataset2/test/images'):
#    im = cv2.imread('datasets/dataset2/test/images/{}'.format(f))[..., ::-1]  # OpenCV image (BGR to RGB)
#    images.append(im)

# Inference
results = model(imgs) # batch of images

# Results
#results.print()  
results.save('results')  # or .show()

#results.xyxy[0]  # im1 predictions (tensor)
#results.pandas().xyxy[0]  # im1 predictions (pandas)