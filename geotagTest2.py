import math
import numpy as np

# Drone position
drone_lat = 21.4004066999989
drone_lon = -157.764462099997
drone_alt = 19.373

# Camera parameters
fov = 83  # field of view in degrees
pitch = -0.026569455862045288  # pitch angle in degrees
yaw = 1.3217555284500122  # yaw angle in degrees
roll = -0.03365262970328331  # roll angle in degrees

# Target position in image
target_x = 4890
target_y = 1580

# Image parameters
image_width = 6000
image_height = 4000
resolution = 3.91e-9 # meters per pixel

# Calculate horizontal and vertical angles from drone to target
h_angle = math.atan((target_x - image_width / 2) * resolution)
v_angle = math.atan((target_y - image_height / 2) * resolution)

# Calculate target distance from drone
distance = drone_alt / math.cos(v_angle)

# Calculate target position in drone coordinates
x = distance * math.sin(h_angle)
y = distance * math.cos(h_angle) * math.sin(v_angle)
z = -distance * math.cos(h_angle) * math.cos(v_angle)

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

# Convert target position to earth coordinates
X, Y, Z = R @ [x, y, z]
lat = drone_lat + math.degrees(Y / 111319.9)
lon = drone_lon + math.degrees(X / (111319.9 * math.cos(math.radians(drone_lat))))

# Print result with 2 meter precision
print(f"Target position: ({lat}, {lon})")