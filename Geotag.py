import math


lat = 21.4010136
long = -157.7640182
alt = 88
head = 35.92783
pitch = 8.915909
roll = 2.609586
mnt_angle = 0
hor_fov = 73.7
ver_fov = 53.1




def x(altitude, roll):
   radians = roll * math.pi / 180
   return altitude * math.tan(radians)




def y(altitude, pitch):
   radians = pitch * math.pi / 180
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
   radians1 = radians = math.asin(math.sin(latitude) * math.cos(
       (altitude * math.tan(camera_mount_angle) / 6378137) + math.cos(latitude) * math.sin(
           altitude * math.tan(camera_mount_angle) / 6378137) * math.cos(heading)))
   radians = longitude + math.atan2(
       math.sin(heading) * math.sin((altitude * math.tan(camera_mount_angle)) / 6378137) * math.cos(latitude),
       math.cos((altitude * math.tan(camera_mount_angle)) / 6378137) - math.sin(latitude) * math.sin(latitude_angle))


   return radians * 180 / math.pi




# print(matts_longitude(0.3735181506, lat, long, alt, mnt_angle, head))
# =ASIN(SIN(C3)*COS((B5*TAN(C9)/6378137)+COS(C3)*SIN(B5*TAN(C9)/6378137)*COS(C6)))
# =math.(SIN(C3)*COS((B5*TAN(C9)/6378137)+COS(C3)*SIN(B5*TAN(C9)/6378137)*COS(C6)))


def center_latitude(latitude, x, y, heading):
   latitude = latitude * math.pi / 180
   heading = heading * math.pi / 180
   dist = distance(x, y)
   radians = math.asin(math.sin(latitude) * math.cos(dist / 6378137) +
                       math.cos(latitude) * math.sin(dist / 6378137) * math.cos(math.atan2(y, x) + heading))
   return radians * 180 / math.pi




# print(center_latitude(21.4010136, 4.010810128, 13.805467, head))


def center_longitude(longitude, latitude, center_latitude, heading, x, y):
   longitude = longitude * math.pi / 180
   latitude = latitude * math.pi / 180
   heading = heading * math.pi / 180
   x1 = math.cos(distance(x, y)/6378137)-math.sin(latitude)*math.sin(center_latitude)
   y1 = math.sin(math.atan2(y,x)+heading)*math.sin(distance(x, y)/6378137)*math.cos(latitude)
   return longitude + math.atan2(y1, x1)






#print(center_longitude(long, lat, 0.3735173897, head, 4.010810128, 13.805467))

