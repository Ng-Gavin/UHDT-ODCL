from Geotag import geotag, geotag1, geotag2, geotag3
def geotag_print(expectedLat, expectedLon, testMetaData, target_x, target_y):
    config = {
        'image_width': 6000,
        'image_height': 4000,
        'resolution': 3.91e-9
    }
    print('Geo 1')
    geo1 = geotag1(config, testMetaData, target_x, target_y)
    print(geo1)
    print(geo1[0] - expectedLat, geo1[1] - expectedLon)
    print('Geo 2')
    geo2 = geotag1(config, testMetaData, target_x, target_y)
    print(geo2)
    print(geo2[0] - expectedLat, geo2[1] - expectedLon)
    print('Geo 3')
    geo3 = geotag3(config, testMetaData, target_x, target_y)
    print(geo3)
    print(geo3[0] - expectedLat, geo3[1] - expectedLon)
    print('Geo Avg')
    geo = geotag(config, testMetaData, target_x, target_y)
    print(geo)
    print(geo[0] - expectedLat, geo[1] - expectedLon)

# Circle
print('Circle')
geotag_print(21.400389, -157.764566, (-0.026569455862045288, 1.3217555284500122, -0.03365262970328331, 21.4004066999989, 157.764462099997, 19.373, 32.8807868165728), 4890, 1580)

# Octagon
print('Octagon')
geotag_print(21.400354, -157.764322, (-0.0855364203453064, 1.2410184144973755, 0.02157663367688656, 21.4003061000022, 157.764225299983, 24.913, 32.8807868165728), 426, 2132)