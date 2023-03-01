import cv2
import torch
import os
from PIL import Image
import ObjectDetection

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/2.pt')
model.conf = 0.85
model.multi_label = False
model.max_det = 5

def ObjectDetection(image):
    results = model(image, size=[1280,1280])
    crops = results.crop(save=False)
    return crops, results;

for Bfiles in os.listdir('datasets/dataset3/test/images/'):
    image = Image.open(f'datasets/dataset3/test/images/{Bfiles}')
    crop, results = ObjectDetection(image)
    results.print()