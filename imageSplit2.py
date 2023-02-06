import os
import cv2
img_h = 4000;
img_w = 6000;
frmt = 'jpeg'

for Bfiles in os.listdir('background'):
    print(Bfiles)    
    img = cv2.imread("background/{}".format(Bfiles))
    name, fext = os.path.splitext(Bfiles)
    split1 = img[0:1280*2, 0:1280*3]
    split2 = img[0:1280*2, img_w-1280*3:img_w]
    split3 = img[img_h-1280*2:img_h, 0:1280*3]
    split4 = img[img_h-1280*2:img_h, img_w-1280*3:img_w]
    cv2.imwrite('backgroundSplit/{}_split1.{}'.format(name, frmt), split1)
    cv2.imwrite('backgroundSplit/{}_split2.{}'.format(name, frmt), split2)
    cv2.imwrite('backgroundSplit/{}_split3.{}'.format(name, frmt), split3)
    cv2.imwrite('backgroundSplit/{}_split4.{}'.format(name, frmt), split4)