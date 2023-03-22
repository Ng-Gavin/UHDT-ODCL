import cv2
import re
import pytesseract
from pytesseract import Output
from PIL import Image


custom_config = ("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 13"
                  " -l UHDT"
                  " ")

#this function just returns the letter/characters that is being read
def image2text(img):
    letter=pytesseract.image_to_string(img, config=custom_config)
    return letter

#this fucntion returns an array with the the letter as the first value and the confidence value as the 2nd value
def image2textConf(img):
    text = []
    results=pytesseract.image_to_data(img, config=custom_config, output_type=Output.DICT)
    text.append(results["text"][len(results["text"])-1])
    text.append(results["conf"][len(results["text"])-1])
    return text

