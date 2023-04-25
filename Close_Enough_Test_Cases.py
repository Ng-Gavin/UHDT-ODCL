#shape might be a number rather than in english (for now)
class Target:
    def __init__(self, shape, latitude, longitude, shapeColor, alphanumColor, alphanum):
        self.shape = shape
        self.latitude = latitude
        self.longitude = longitude
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum
    def __str__(self):
        return(f'shape = {self.shape}; latitude = {self.latitude}; longitude = {self.longitude}; shapecolor = {self.shapeColor}; alphcolor = {self.alphanumColor}; alphanum = {self.alphanum};')
class Payload:
    def __init__(self, dock, shape, shapeColor, alphanumColor, alphanum):
        self.dock = dock
        self.shape = shape
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum
    def __str__(self):
        return(f'dock = {self.dock}; shape = {self.shape}; shapecolor = {self.shapeColor}; alphcolor = {self.alphanumColor}; alphanum = {self.alphanum};')
    
'''
def class_to_shape(shape):
    switcher = {
        0: "quartercircle",
        1: "triangle",
        2: "cross",
        3: "star",
        4: "square",
        5: "rectangle",
        6: "semicircle",
        7: "trapezoid",
        8: "pentagon",
        9: "hexagon",
        10: "heptagon",
        11: "octagon",
        12: "circle"
    }
    return switcher.get(shape, "nothing")
'''

def compare(payload, target):
    #assuming shapes come in as numbers (can prob reverse the switch statement if not)
    score = 0;
    diff = abs(payload.shape - target.shape);
    #shape
    if diff == 0:
        score += 1
    else:
        score += (1/diff)
    #alphanum color
    if payload.alphanumColor == target.alphanumColor:
        score += 1
    #alphanum
    if payload.alphanum == target.alphanum:
        score += 1
    return score

#changed shapes to numbers
targets = []
targets.append(Target(1, 9, 9, 'no', 'mbrah', 'y'))
targets.append(Target(1, 9, 8, 'no', 'mbrah', 'no'))
targets.append(Target(1, 9, 9, 'no', 'mbrah', 'z'))
targets.append(Target(1, 9, 8, 'no', 'mbrah', '8'))
targets.append(Target(1, 9, 9, 'no', 'mbrah', '20'))

payloads = []
payloads.append(Payload(1, 1,'no', 'mbrah', 'no'))
payloads.append(Payload(2, 3, 'no', 'mbrah', 'y'))
payloads.append(Payload(3, 1,'no', 'mbrah', 'z'))
payloads.append(Payload(4, 1, 'no', 'mbrah', '8'))
payloads.append(Payload(5, 1,'no', 'mbrah', '20'))

print(compare(payloads[1],targets[1]))

def match_targets(payloads, targets):
    target_order = []
    for payload in payloads:
        scores = []
        for target in targets:
            score = compare(payload, target)
            scores.append(score)
        print(f'Payload in Dock #{payloads.index(payload)} corresponds to Target #{scores.index(max(scores))}')
        target_order.append(targets[scores.index(max(scores))])
    return target_order

match_targets(payloads, targets)






