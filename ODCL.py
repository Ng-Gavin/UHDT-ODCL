import os
from PIL import Image
import time
from ColorRec import color_rec as CR
from AlphanumRec import image2textConf as AR
from ObjectDetection import ObjectDetection
from ObjectDetection import class_to_shape
import TargetClass
from metadataExtractor import dataExtract as dataExtract
from payloadDelivery import deliveryScript as deliveryScript

#Payload 1 Info
dock1 = 1
shape1 = ""
shapeColor1 = "" 
alphanumColor1 = ""
alphanum1 = ""

#Payload 2 Info
dock2 = 2
shape2 = ""
shapeColor2 = "" 
alphanumColor2 = ""
alphanum2 = ""

#Payload 3 Info
dock3 = 3
shape3 = ""
shapeColor3 = "" 
alphanumColor3 = ""
alphanum3 = ""

#Payload 4 Info
dock4 = 4
shape4 = ""
shapeColor4 = "" 
alphanumColor4 = ""
alphanum4 = ""

#Payload 5 Info
dock5 = 5
shape5 = ""
shapeColor5 = "" 
alphanumColor5 = ""
alphanum5 = ""

num = 1
iter = 0 #Number of pictures to run through
start = time.time()
testDir = 'datasets/dataset4/test/images/'
targetList = []
payloadlist = []
path = 'watchdog'

def watch_directory():
    print("File Watcher Initiated")
    while len(targetList) < 5:
        for filename in os.listdir(path):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                full_path = os.path.join(path, filename)
                # Wait until the file is fully created
                while True:
                    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
                        break
                    time.sleep(1)
                # Process the image file
                ODCL(full_path)
                # Delete the image file
                os.remove(full_path)
        time.sleep(3) # Check directory every __ seconds
    if(len(targetList) >= 5):
        deliveryScript()

def ODCL(image):
    #if iter >= num:
    #    break
    image = Image.open(f'{image}')
    latitude, longitude, pitch, yaw, roll, altitude = dataExtract(f'{image}')
    #image.show()
    results, crops, bboxes = ObjectDetection(image)
    #print(bboxes)
    for bbox in bboxes:
        x1, y1, x2, y2, conf, shape = bbox
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        xMid,yMid = (x1+x2)/2, (y1+y2)/2  
        cropped = image.crop((x1,y1,x2,y2))
        cropped.show()
        #cropped.save(f'test{iter}.png')
        print(class_to_shape(shape))
        
        #Color Recognition Function Call
        alphanum_string, shape_string, alphanum_rgb, shape_rgb, third_string, third_rgb, filtered = CR(cropped)
        
        #Alphanumeric Recognition Function Call
        alphanum, alphanum_conf = AR(filtered)
        
        
        #print(alphanum_string, shape_string, alphanum_rgb, shape_rgb, third_string, third_rgb)
        print(alphanum, alphanum_conf)

    #results.save(save_dir='results/test/')
    #crop.show()
    #iter += 1


payload1 = TargetClass.Payload(dock1, shape1, shapeColor1, alphanumColor1, alphanum1); payloadlist.append(payload1); print("Payload 1 Added")
payload2 = TargetClass.Payload(dock2, shape2, shapeColor2, alphanumColor2, alphanum2); payloadlist.append(payload2); print("Payload 2 Added")
payload3 = TargetClass.Payload(dock3, shape3, shapeColor3, alphanumColor3, alphanum3); payloadlist.append(payload3); print("Payload 3 Added")
payload4 = TargetClass.Payload(dock4, shape4, shapeColor4, alphanumColor4, alphanum4); payloadlist.append(payload4); print("Payload 4 Added")
payload5 = TargetClass.Payload(dock5, shape5, shapeColor5, alphanumColor5, alphanum5); payloadlist.append(payload5); print("Payload 5 Added")

watch_directory()

end = time.time()
print("Runtime:",end - start)

