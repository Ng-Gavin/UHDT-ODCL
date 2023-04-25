import math

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

def compare_color(payload_color, target_color):
    from colormath.color_objects import sRGBColor, LabColor
    from colormath.color_conversions import convert_color
    from deltae2000 import delta_e_cie2000
    color1_lab = 0;
    color2_lab = 0;
    if (payload_color == 'RED'):
        payload_color_rgb = sRGBColor(255, 0, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'ORANGE'):
        payload_color_rgb = sRGBColor(255, 128, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'YELLOW'):
        payload_color_rgb = sRGBColor(255, 255, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'GREEN'):
        payload_color_rgb = sRGBColor(0, 255, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'BLUE'):
        payload_color_rgb = sRGBColor(0, 0, 255)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'PURPLE'):
        payload_color_rgb = sRGBColor(128, 0, 128)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'BLACK'):
        payload_color_rgb = sRGBColor(0, 0, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'WHITE'):
        payload_color_rgb = sRGBColor(255, 255, 255)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    elif (payload_color == 'GRAY'):
        payload_color_rgb = sRGBColor(128, 128, 128)
        color1_lab = convert_color(payload_color_rgb, LabColor)
    else: # Brown
        payload_color_rgb = sRGBColor(150, 75, 0)
        color1_lab = convert_color(payload_color_rgb, LabColor)

    if (target_color == 'RED'):
        target_color_rgb = sRGBColor(255, 0, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'ORANGE'):
        target_color_rgb = sRGBColor(255, 128, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'YELLOW'):
        target_color_rgb = sRGBColor(255, 255, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'GREEN'):
        target_color_rgb = sRGBColor(0, 255, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'BLUE'):
        target_color_rgb = sRGBColor(0, 0, 255)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'PURPLE'):
        target_color_rgb = sRGBColor(128, 0, 128)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'BLACK'):
        target_color_rgb = sRGBColor(0, 0, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'WHITE'):
        target_color_rgb = sRGBColor(255, 255, 255)
        color2_lab = convert_color(target_color_rgb, LabColor)
    elif (target_color == 'GRAY'):
        target_color_rgb = sRGBColor(128, 128, 128)
        color2_lab = convert_color(target_color_rgb, LabColor)
    else: # Brown
        target_color_rgb = sRGBColor(150, 75, 0)
        color2_lab = convert_color(target_color_rgb, LabColor)

    # Finding the difference
    diff = abs(0.001*(1000-delta_e_cie2000(color1_lab, color2_lab)))
    return diff


def compare(payload, target):
    #assuming shapes come in as numbers (can prob reverse the switch statement if not)
    score = 0;
    diff = abs(payload.shape - target.shape);
    #shape
    if diff == 0:
        score += 1
    else:
        score += (1/diff)
    #shape_color
    if payload.shapeColor == target.shapeColor:
        score += 1
    else:
        score += compare_color(payload.shapeColor, target.shapeColor)
    #alphanum color
    if payload.alphanumColor == target.alphanumColor:
        score += 1
    else:
        score += compare_color(payload.alphanumColor, target.alphanumColor)
    #alphanum
    if payload.alphanum == target.alphanum:
        score += 1
    return score






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

def close_enough_test_cases(drone_lat, drone_lon, payloads, targets):
    sorted_targets = sort_targets(targets, drone_lat, drone_lon)
    return order_payloads(payloads, sorted_targets)









