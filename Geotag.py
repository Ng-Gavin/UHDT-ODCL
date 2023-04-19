import math
import numpy as np

# All function angle inputs are assumed to be in degrees and converted to radians within the function

# Pass in config object with image_width, image_height, and resolution properties:
# config = {
#      'image_width': 6000,
#      'image_height': 4000,
#      'resolution': 3.91e-9
# }

# metadata tuple from the metadataExtractor.py will be passed in the order of pitch, yaw, roll, drone_latitude, drone_longitude, drone_altitude, fov:

# Calculate the x-coordinate of the target in meters
def calculate_x(image_width, resolution, target_x):
    return (target_x - image_width / 2) * resolution

# Calculate the y-coordinate in meters
def calculate_y(image_height, resolution, target_y):
    return (target_y - image_height / 2) * resolution

# Calculate the angle
def angle(x, y):
    return math.atan2(y, x)

# Calculate the distance of the target
def distance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Alternative to the center latitude formula
def matts_latitude(drone_latitude, altitude, camera_mount_angle, heading):
    latitude = drone_latitude * math.pi / 180
    camera_mount_angle = camera_mount_angle * math.pi / 180
    heading = heading * math.pi / 180
    radians = math.asin(math.sin(latitude) * math.cos(
        (altitude * math.tan(camera_mount_angle) / 6378137) + math.cos(latitude) * math.sin(
            altitude * math.tan(camera_mount_angle) / 6378137) * math.cos(heading)))
    return radians * 180 / math.pi

# Alternative to the center longitude formula
def matts_longitude(latitude_angle, drone_latitude, drone_longitude, altitude, camera_mount_angle, yaw):
    latitude = drone_latitude * math.pi / 180
    longitude = drone_longitude * math.pi / 180
    camera_mount_angle = camera_mount_angle * math.pi / 180
    heading = yaw * math.pi / 180
    radians = math.asin(math.sin(latitude) * math.cos(
        (altitude * math.tan(camera_mount_angle) / 6378137) + math.cos(latitude) * math.sin(
            altitude * math.tan(camera_mount_angle) / 6378137) * math.cos(heading)))
    radians = longitude + math.atan2(
        math.sin(heading) * math.sin((altitude *
                                      math.tan(camera_mount_angle)) / 6378137) * math.cos(latitude),
        math.cos((altitude * math.tan(camera_mount_angle)) / 6378137) - math.sin(latitude) * math.sin(latitude_angle))
    return radians * 180 / math.pi


def center_latitude(drone_latitude, x, y, yaw):
    latitude = drone_latitude * math.pi / 180
    heading = yaw * math.pi / 180
    dist = distance(x, y)
    radians = math.asin(math.sin(latitude) * math.cos(dist / 6378137) +
                        math.cos(latitude) * math.sin(dist / 6378137) * math.cos(math.atan2(y, x) + heading))
    return radians * 180 / math.pi


def center_longitude(drone_longitude, drone_latitude, center_latitude, yaw, x, y):
    longitude = drone_longitude * math.pi / 180
    latitude = drone_latitude * math.pi / 180
    heading = yaw * math.pi / 180
    x1 = math.cos(distance(x, y)/6378137) - \
        math.sin(latitude)*math.sin(center_latitude)
    y1 = math.sin(math.atan2(y, x)+heading) * \
        math.sin(distance(x, y)/6378137)*math.cos(latitude)
    return 180 / math.pi * (-longitude + math.atan2(y1, x1))

def geotag1(config, metadata, target_x, target_y):
    image_width, image_height, resolution = config.values()
    pitch, yaw, roll, drone_latitude, drone_longitude, drone_altitude, fov = metadata
    drone_longitude = -drone_longitude
    # Calculate image dimensions in meters
    W = 2 * drone_altitude * math.tan(math.radians(fov / 2))
    H = W * image_height / image_width

    # Convert pixel coordinates to meters
    x = (target_x - image_width / 2) * resolution
    y = (target_y - image_height / 2) * resolution

    # Calculate rotation matrix
    R = np.array([
        [math.cos(math.radians(yaw)) * math.cos(math.radians(pitch)),
         math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) - math.sin(
             math.radians(yaw)) * math.cos(math.radians(roll)),
         math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) + math.sin(
             math.radians(yaw)) * math.sin(math.radians(roll))],
        [math.sin(math.radians(yaw)) * math.cos(math.radians(pitch)),
         math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) + math.cos(
             math.radians(yaw)) * math.cos(math.radians(roll)),
         math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) - math.cos(
             math.radians(yaw)) * math.sin(math.radians(roll))],
        [-math.sin(math.radians(pitch)),
         math.cos(math.radians(pitch)) * math.sin(math.radians(roll)),
         math.cos(math.radians(pitch)) * math.cos(math.radians(roll))]
    ])

    # Convert image coordinates to drone coordinates
    X, Y, Z = R @ [x, y, -drone_altitude]

    # Calculate target latitude and longitude
    lat = drone_latitude + math.degrees(Y / 111319.9)
    lon = drone_longitude + math.degrees(X / (111319.9 * math.cos(math.radians(drone_latitude))))

    # Print result with 2 meter precision
    return lat, lon

def geotag2(config, metadata, target_x, target_y):
    image_width, image_height, resolution = config.values()
    pitch, yaw, roll, drone_latitude, drone_longitude, drone_altitude, fov = metadata
    drone_longitude = -drone_longitude
    # Calculate horizontal and vertical angles from drone to target
    h_angle = math.atan((target_x - image_width / 2) * resolution)
    v_angle = math.atan((target_y - image_height / 2) * resolution)

    # Calculate target distance from drone
    distance = drone_altitude / math.cos(v_angle)

    # Calculate target position in drone coordinates
    x = distance * math.sin(h_angle)
    y = distance * math.cos(h_angle) * math.sin(v_angle)
    z = -distance * math.cos(h_angle) * math.cos(v_angle)

    # Calculate rotation matrix
    R = np.array([
        [math.cos(math.radians(yaw)) * math.cos(math.radians(pitch)),
         math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) - math.sin(
             math.radians(yaw)) * math.cos(math.radians(roll)),
         math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) + math.sin(
             math.radians(yaw)) * math.sin(math.radians(roll))],
        [math.sin(math.radians(yaw)) * math.cos(math.radians(pitch)),
         math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) + math.cos(
             math.radians(yaw)) * math.cos(math.radians(roll)),
         math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) - math.cos(
             math.radians(yaw)) * math.sin(math.radians(roll))],
        [-math.sin(math.radians(pitch)),
         math.cos(math.radians(pitch)) * math.sin(math.radians(roll)),
         math.cos(math.radians(pitch)) * math.cos(math.radians(roll))]
    ])

    # Convert target position to earth coordinates
    X, Y, Z = R @ [x, y, z]
    lat = drone_latitude + math.degrees(Y / 111319.9)
    lon = drone_longitude + math.degrees(X / (111319.9 * math.cos(math.radians(drone_latitude))))

    # Print result with 2 meter precision
    return lat, lon

# Calculatures coordinates using the center latitude/longitude formulas
def geotag3(config, metadata, target_x, target_y):
    image_width, image_height, resolution = config.values()
    pitch, yaw, roll, drone_latitude, drone_longitude, drone_altitude, fov = metadata
    x = calculate_x(image_width, resolution, target_x)
    y = calculate_y(image_height, resolution, target_y)
    target_latitude = center_latitude(drone_latitude, x, y, yaw)
    target_longitude = center_longitude(drone_longitude, drone_latitude, target_latitude, yaw, x, y)
    return (target_latitude, target_longitude)

# Averages the coordinate values returned by each of the three geotagging algorithms
def geotag(config, metadata, target_x, target_y):
    lat1, lon1 = geotag1(config, metadata, target_x, target_y);
    lat2, lon2 = geotag2(config, metadata, target_x, target_y);
    lat3, lon3 = geotag3(config, metadata, target_x, target_y);
    lat_avg = sum([lat1, lat2, lat3])/3;
    lon_avg = sum([lon1, lon2, lon3])/3;
    return lat_avg, lon_avg








