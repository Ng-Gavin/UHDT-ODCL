import cv2
import torch
import os
from PIL import Image
import time

testDir = 'datasets/dataset1/test/images/'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/nano.pt')
model.conf = 0.2
model.multi_label = False
model.max_det = 5
#num = 1
iter = 0
start = time.time()

def ObjectDetection(image):
    results = model(image, size=[6000,4000])
    crops = results.crop(save=False)
    bboxes = results.xyxy[0].tolist()
    return results, crops, bboxes



for Bfiles in os.listdir(testDir):
    #if iter >= num:
    #    break
    image = Image.open(f'{testDir}{Bfiles}')
    results, crops, bboxes = ObjectDetection(image)
    print(bboxes)
    #for bbox in bboxes:
    #    x1, y1, x2, y2, conf, class_id = bbox
    #    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    #    cropped = image.crop((x1,y1,x2,y2))
    #    cropped.show()
    results.save(save_dir='results/test/')
    #crop.show()
    iter += 1
end = time.time()
print(end - start)