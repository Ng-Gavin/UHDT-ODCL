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
def X_offset(altitude,hor_fov):
    return altitude*(math.tan((hor_fov*rad_convert)/2))
#Y-offset(corner)
def Y_offset(altitude,vert_fov):
    return altitude*(math.tan((vert_fov*rad_convert)/2))

#dx
def dx1():
    return x(altitude, roll) + X_offset(altitude,hor_fov)
def dx2():
    return x(altitude, roll) - X_offset(altitude,hor_fov)
def dx3():
    return x(altitude, roll) - X_offset(altitude,hor_fov)
def dx4():
    return x(altitude, roll) + X_offset(altitude,hor_fov)

#dy
def dy1():
    return y(altitude, pitch) + Y_offset(altitude,vert_fov)
def dy2(): 
    return y(altitude, pitch) + Y_offset(altitude,vert_fov)
def dy3(): 
    return y(altitude, pitch) - Y_offset(altitude,vert_fov)
def dy4(): 
    return y(altitude, pitch) - Y_offset(altitude,vert_fov)

#heading  (x and y reversed)
def hdg1():
    return math.atan2(dy1(y,altitude,pitch,vert_fov),dy1(y,altitude,pitch,vert_fov)) + (heading*rad_convert)

def hdg2():
    return math.atan2(dy2(y,altitude,pitch,vert_fov),dx2(x,altitude,roll,hor_fov,X_offset)) + (heading*rad_convert)

def hdg3():
    return math.atan2(dy3(y,altitude,pitch,vert_fov),dx3(x,altitude,roll,hor_fov,X_offset)) + (heading*rad_convert)

def hdg4():
    return math.atan2(dy4(y,altitude,pitch,vert_fov),dx4(x,altitude,roll,hor_fov,X_offset)) + (heading*rad_convert)

#distance
def dist1():
    return math.pow((dx1()**2)+(dy1()**2),0.5)
def dist2():
    return math.pow((dx2()**2)+(dy2()**2),0.5)
def dist3():
    return math.pow((dx3()**2)+(dy3()**2),0.5)
def dist4():
    return math.pow((dx4()**2)+(dy4()**2),0.5)
