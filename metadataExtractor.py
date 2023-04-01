from exiftool import ExifToolHelper

pitch = 0
yaw = 0
roll = 0
latitude = 0
longitude = 0

with ExifToolHelper() as et:
    for d in et.get_metadata("real2.jpg"):
        for k, v in d.items():
            #read latitude
            if (k == "EXIF:GPSLatitude"):
                latitude = float(v)
            #read longitude
            if (k == "EXIF:GPSLongitude"):
                longitude = float(v)
            #read comment line containing pitch,yaw,roll
            if (k == "File:Comment"):
                #split up pitch,yaw,roll
                p_y_r = v.split(" ")
                #create empty array to hold value pairs
                p_y_r_vals = []
                #split up the three values into property and number
                for val in p_y_r:
                    p_y_r_vals.append(val.split(":"))
                #take the numbers from each property and assign to variables
                pitch = float(p_y_r_vals[0][1])
                yaw = float(p_y_r_vals[1][1])
                roll = float(p_y_r_vals[2][1])
