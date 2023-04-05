from exiftool import ExifToolHelper

def extractMetadata(fileName):
    with ExifToolHelper() as et:
        metadata = et.get_tags(fileName, ['Comment', 'GPSLatitude', 'GPSLongitude', 'GPSAltitude'])[0]
        comment = metadata['File:Comment'].split(' ')
        comment_data = [x.split(':') for x in comment]
        pitch = float(comment_data[0][1])
        yaw = float(comment_data[1][1])
        roll = float(comment_data[2][1])
        latitude = metadata['EXIF:GPSLatitude']
        longitude = metadata['EXIF:GPSLongitude']
        altitude = metadata['EXIF:GPSAltitude']
        return pitch, yaw, roll, latitude, longitude, altitude


print(extractMetadata('real18.jpg'))