import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/nano.pt')
model.conf = 0.2
model.multi_label = False
model.max_det = 5

def ObjectDetection(image):
    width, height = image.size
    results = model(image, size=[width,height])
    crops = results.crop(save=False)
    bboxes = results.xyxy[0].tolist()
    return results, crops, bboxes

def class_to_shape(shape):
    switcher = {
        0: "circle",
        1: "cross",
        2: "heptagon",
        3: "hexagon",
        4: "octagon",
        5: "pentagon",
        6: "quartercircle",
        7: "rectangle",
        8: "semicircle",
        9: "square",
        10: "star",
        11: "trapezoid",
        12: "triangle"
    }
    return switcher.get(shape, "nothing")