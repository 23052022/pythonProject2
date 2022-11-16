import math

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return  Coord(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

def line_length(point1, point2):
    return math.sqrt((point1.x+point2.x)**2 + (point1.y+point2.y)**2)
