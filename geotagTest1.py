import math
import numpy as np

# Drone position
drone_lat = 21.4004066999989
drone_lon = -157.764462099997
drone_alt = 19.373

# Camera parameters
fov =  32.8807868165728#83  # field of view in degrees
pitch = -0.02656945586 #-0.026569455862045288  # pitch angle in degrees
yaw = 1.321755528#1.3217555284500122  # yaw angle in degrees
roll = -0.0336526297#-0.03365262970328331  # roll angle in degrees

# Target position in image
target_x = 4890
target_y = 1580

# Image parameters
image_width = 6000

image_height = 4000
resolution = 3.91e-9 # meters per pixel

# Calculate image dimensions in meters
W = 2 * drone_alt * math.tan(math.radians(fov / 2))
H = W * image_height / image_width

# Convert pixel coordinates to meters
x = (target_x - image_width / 2) * resolution
y = (target_y - image_height / 2) * resolution

# Calculate rotation matrix
R = np.array([
    [math.cos(math.radians(yaw)) * math.cos(math.radians(pitch)),
     math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) - math.sin(math.radians(yaw)) * math.cos(math.radians(roll)),
     math.cos(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) + math.sin(math.radians(yaw)) * math.sin(math.radians(roll))],
    [math.sin(math.radians(yaw)) * math.cos(math.radians(pitch)),
     math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.sin(math.radians(roll)) + math.cos(math.radians(yaw)) * math.cos(math.radians(roll)),
     math.sin(math.radians(yaw)) * math.sin(math.radians(pitch)) * math.cos(math.radians(roll)) - math.cos(math.radians(yaw)) * math.sin(math.radians(roll))],
    [-math.sin(math.radians(pitch)),
     math.cos(math.radians(pitch)) * math.sin(math.radians(roll)),
     math.cos(math.radians(pitch)) * math.cos(math.radians(roll))]
])

# Convert image coordinates to drone coordinates
X, Y, Z = R @ [x, y, -drone_alt]

# Calculate target latitude and longitude
lat = drone_lat + math.degrees(Y / 111319.9)
lon = drone_lon + math.degrees(X / (111319.9 * math.cos(math.radians(drone_lat))))

# Print result with 2 meter precision
print(f"Target position: ({lat}, {lon})")