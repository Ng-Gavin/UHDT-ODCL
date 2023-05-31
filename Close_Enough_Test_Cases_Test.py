import math


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
targets.append(Target('mbruh', 10, 9, 'no', 'mbrah', 'y'))
targets.append(Target('mbruh', 9, 8, 'no', 'mbrah', 'no'))
targets.append(Target('mbruh', 9, 9, 'no', 'mbrah', 'z'))
targets.append(Target('mbruh', 9, 8, 'no', 'mbrah', '8'))
targets.append(Target('mbruh', 9, 9, 'no', 'mbrah', '20'))

payloads = []
payloads.append(Payload(1, 'mbruh','no', 'mbrah', 'no'))
payloads.append(Payload(2, 'mbruh', 'no', 'mbrah', 'y'))
payloads.append(Payload(3, 'mbruh','no', 'mbrah', '8'))
payloads.append(Payload(4, 'mbruh', 'no', 'mbrah', 'z'))
payloads.append(Payload(5, 'mbruh','no', 'mbrah', 'z'))


def calculate_dist(drone_lat, drone_lon, target_lat, target_lon):
    dLat = (target_lat-drone_lat) * math.pi / 180
    dLon = (target_lon-drone_lon)*math.pi/180
    lat1 = drone_lat * math.pi / 180
    lat2 = target_lat * math.pi / 180
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return c

test_targets = [{'latitude': 1, 'longitude': 1}, {'latitude': 3, 'longitude': 3}, {'latitude': 2, 'longitude': 2}, {'latitude': 5, 'longitude': 5}, {'latitude': 4, 'longitude': 4}]

def sort_targets(targets, drone_lat, drone_lon):
    sorted_targets = []
    target_order = [];
    for i in range(len(targets)):
        target_lat = targets[i]['latitude']
        target_lon = targets[i]['longitude']
        target_distance = calculate_dist(drone_lat, drone_lon, target_lat, target_lon);
        target_order.append([target_distance, i])
    target_order.sort()
    for order in target_order:
        index = order[1]
        sorted_targets.append(targets[index])

    return sorted_targets
#print(targets)
#print(sort_targets(test_targets, 6, 6))


def order_payloads(payloads, targets):
    payload_order = []
    target_scores = []
    hasConflicts = False
    unassigned_targets = []
    unassigned_payloads = [0, 1, 2, 3, 4]
    ordered_payloads = []

    for target in targets:
        payload_scores = []
        for payload in payloads:
            payload_score = compare(payload, target)
            payload_scores.append(payload_score)
        target_scores.append(payload_scores)

    for payload_scores in target_scores:
        payload_order.append(payload_scores.index(max(payload_scores)))

    for index in payload_order:
        if payload_order.count(index) > 1: hasConflicts = True
        else: hasConflicts = False

    if hasConflicts:
        for i in range(len(payload_order)):
            if payload_order.count(payload_order[i]) != 1:
                unassigned_targets.append(i)
            if payload_order.count(payload_order[i]) == 1:
                unassigned_payloads.remove(payload_order[i])
            for j in range(len(unassigned_targets)):
                payload_order[unassigned_targets[j]] = unassigned_payloads[j]
        for payload_index in payload_order:
            ordered_payloads.append(payloads[payload_index])
    else:
        for payload_index in payload_order:
            ordered_payloads.append(payloads[payload_index])
    return ordered_payloads










