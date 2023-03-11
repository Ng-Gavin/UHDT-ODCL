import math

#set variable for converting to pi
rad_convert = math.pi/180
# All function angle inputs are assumed to be in degrees and converted to radians within the function


def x(altitude, roll):
    radians = roll * rad_convert
    return altitude * math.tan(radians)


def y(altitude, pitch):
    radians = pitch * rad_convert
    return altitude * math.tan(radians)


def angle(x, y):
    return math.atan2(y, x)


def distance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def matts_latitude(latitude, altitude, camera_mount_angle, heading):
    latitude = latitude * math.pi / 180
    camera_mount_angle = camera_mount_angle * math.pi / 180
    heading = heading * math.pi / 180
    radians = math.asin(math.sin(latitude) * math.cos(
        (altitude * math.tan(camera_mount_angle) / 6378137) + math.cos(latitude) * math.sin(
            altitude * math.tan(camera_mount_angle) / 6378137) * math.cos(heading)))
    return radians * 180 / math.pi


def matts_longitude(latitude_angle, latitude, longitude, altitude, camera_mount_angle, heading):
    latitude = latitude * math.pi / 180
    longitude = longitude * math.pi / 180
    camera_mount_angle = camera_mount_angle * math.pi / 180
    heading = heading * math.pi / 180
    radians = math.asin(math.sin(latitude) * math.cos(
        (altitude * math.tan(camera_mount_angle) / 6378137) + math.cos(latitude) * math.sin(
            altitude * math.tan(camera_mount_angle) / 6378137) * math.cos(heading)))
    radians = longitude + math.atan2(
        math.sin(heading) * math.sin((altitude *
                                      math.tan(camera_mount_angle)) / 6378137) * math.cos(latitude),
        math.cos((altitude * math.tan(camera_mount_angle)) / 6378137) - math.sin(latitude) * math.sin(latitude_angle))
    return radians * 180 / math.pi


def center_latitude(latitude, x, y, heading):
    latitude = latitude * math.pi / 180
    heading = heading * math.pi / 180
    dist = distance(x, y)
    radians = math.asin(math.sin(latitude) * math.cos(dist / 6378137) +
                        math.cos(latitude) * math.sin(dist / 6378137) * math.cos(math.atan2(y, x) + heading))
    return radians * 180 / math.pi


def center_longitude(longitude, latitude, center_latitude, heading, x, y):
    longitude = longitude * math.pi / 180
    latitude = latitude * math.pi / 180
    heading = heading * math.pi / 180
    x1 = math.cos(distance(x, y)/6378137) - \
        math.sin(latitude)*math.sin(center_latitude)
    y1 = math.sin(math.atan2(y, x)+heading) * \
        math.sin(distance(x, y)/6378137)*math.cos(latitude)
    return longitude + math.atan2(y1, x1)

#constants

#assuming hor_v and vert_v are in degrees
#X-offset(corner)
X_offset = altitude*(math.tan((hor_fov*rad_convert)/2))
#Y-offset(corner)
Y_offset = altitude*(math.tan((vert_fov*rad_convert)/2))

#dx
dx1 = x(altitude, roll) + X_offset
dx2 = x(altitude, roll) - X_offset
dx3 = x(altitude, roll) - X_offset
dx4 = x(altitude, roll) + X_offset

#dy
dy1 = y(altitude, pitch) + Y_offset
dy2 = y(altitude, pitch) + Y_offset
dy3 = y(altitude, pitch) - Y_offset
dy4 = y(altitude, pitch) - Y_offset

#heading  (x and y reversed)
hdg1 = math.atan2(dy1,dx1) + (heading*rad_convert)
hdg2 = math.atan2(dy2,dx2) + (heading*rad_convert)
hdg3 = math.atan2(dy3,dx3) + (heading*rad_convert)
hdg4 = math.atan2(dy4,dx4) + (heading*rad_convert)

#distance
dist1 = math.pow((dx1**2)+(dy1**2),0.5)
dist2 = math.pow((dx2**2)+(dy2**2),0.5)
dist3 = math.pow((dx3**2)+(dy3**2),0.5)
dist4 = math.pow((dx4**2)+(dy4**2),0.5)
