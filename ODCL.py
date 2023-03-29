import cv2
import torch
import os
from PIL import Image
<<<<<<< Updated upstream
import ObjectDetection
=======
import time
from ColorRec import color_rec as CR
from AlphanumRec import image2textConf as AR
>>>>>>> Stashed changes

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/2.pt')
model.conf = 0.85
model.multi_label = False
model.max_det = 5
<<<<<<< Updated upstream
=======
num = 2
iter = 0 #Number of pictures to run through
start = time.time()
>>>>>>> Stashed changes

def ObjectDetection(image):
    results = model(image, size=[1280,1280])
    crops = results.crop(save=False)
    return crops, results;

<<<<<<< Updated upstream
for Bfiles in os.listdir('datasets/dataset3/test/images/'):
    image = Image.open(f'datasets/dataset3/test/images/{Bfiles}')
    crop, results = ObjectDetection(image)
    results.print()
=======


for Bfiles in os.listdir(testDir):
    if iter >= num:
        break
    image = Image.open(f'{testDir}{Bfiles}')
    results, crops, bboxes = ObjectDetection(image)
    print(bboxes)
    for bbox in bboxes:
        x1, y1, x2, y2, conf, class_id = bbox
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cropped = image.crop((x1,y1,x2,y2))
        cropped.show()
        #cropped.save(f'test{iter}.png')
        
        #Color Recognition Function Call
        alphanum_string, shape_string, alphanum_rgb, shape_rgb, third_string, third_rgb, filtered = CR(cropped)
        
        #Alphanumeric Recognition Function Call
        alphanum, alphanum_conf = AR(filtered)
        
        
        #print(alphanum_string, shape_string, alphanum_rgb, shape_rgb, third_string, third_rgb)
        #print(alphanum, alphanum_conf)

    #results.save(save_dir='results/test/')
    #crop.show()
    iter += 1
end = time.time()
print(end - start)
>>>>>>> Stashed changes
