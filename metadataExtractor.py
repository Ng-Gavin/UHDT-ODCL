from exiftool import ExifToolHelper


def extractMetadata(fileName):
    with ExifToolHelper() as et:
        metadata = et.get_tags(fileName, ['Comment', 'GPSLatitude', 'GPSLongitude', 'GPSAltitude', 'FOV'])[0]
        comment = metadata['File:Comment'].split(' ')
        comment_data = [x.split(':') for x in comment]
        pitch = float(comment_data[0][1])
        yaw = float(comment_data[1][1])
        roll = float(comment_data[2][1])
        drone_latitude = metadata['EXIF:GPSLatitude']
        drone_longitude = metadata['EXIF:GPSLongitude']
        drone_altitude =  metadata['EXIF:GPSAltitude']
        fov = metadata['Composite:FOV']
        return pitch, yaw, roll, drone_latitude, drone_longitude, drone_altitude, fov


