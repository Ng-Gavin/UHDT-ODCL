class Target:
    def __init__(self, shape, latitude, longitude, shapeColor, alphanumColor, alphanum):
        self.shape = shape
        self.latitude = latitude
        self.longitude = longitude
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum

class Payload:
    def __init__(self, dock, shape, shapeColor, alphanumColor, alphanum):
        self.dock = dock
        self.shape = shape
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum

def compare(payload, target):
    score = 0;
    if payload.shape == target.shape:
        score += 1
    if payload.shapeColor == target.shapeColor:
        score += 1
    if payload.alphanumColor == target.alphanumColor:
        score += 1
    if payload.alphanum == target.alphanum:
        score += 1
    return score

targets = []
targets.append(Target('mbruh', 9, 9, 'no', 'mbrah', 'y'))
targets.append(Target('mbruh', 9, 8, 'no', 'mbrah', 'no'))
targets.append(Target('mbruh', 9, 9, 'no', 'mbrah', 'z'))
targets.append(Target('mbruh', 9, 8, 'no', 'mbrah', '8'))
targets.append(Target('mbruh', 9, 9, 'no', 'mbrah', '20'))

payloads = []
payloads.append(Payload(1, 'mbruh','no', 'mbrah', 'no'))
payloads.append(Payload(2, 'mbruh', 'no', 'mbrah', 'y'))
payloads.append(Payload(3, 'mbruh','no', 'mbrah', 'z'))
payloads.append(Payload(4, 'mbruh', 'no', 'mbrah', '8'))
payloads.append(Payload(5, 'mbruh','no', 'mbrah', '20'))

def match_targets(payloads, targets):
    target_order = []
    for payload in payloads:
        scores = []
        for target in targets:
            score = compare(payload, target)
            scores.append(score)
        #print(f'Payload in Dock #{payloads.index(payload)} corresponds to Target #{scores.index(max(scores))}')
        target_order.append(targets[scores.index(max(scores))])
    return target_order

match_targets(payloads, targets)






