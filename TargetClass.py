class Target:
    def __init__(self, shape, latitude, longitude, shapeColor, alphanumColor, alphanum):
        self.shape = shape
        self.latitude = latitude
        self.longitude = longitude
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum

    def __str__(self):
        return(f'shape = {self.shape}; latitude = {self.latitude}; longitude = {self.longitude}; shapecolor = {self.shapeColor}; alphcolor = {self.alphanumColor}; alphanum = {self.alphanum};')

class Payload:
    def __init__(self, dock, shape, shapeColor, alphanumColor, alphanum):
        self.dock = dock
        self.shape = shape
        self.shapeColor = shapeColor
        self.alphanumColor = alphanumColor
        self.alphanum = alphanum

    def __str__(self):
        return(f'dock = {self.dock}; shape = {self.shape}; shapecolor = {self.shapeColor}; alphcolor = {self.alphanumColor}; alphanum = {self.alphanum};')
