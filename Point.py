
#class with coordinate attributes , initialize with coordinates,
#give coordinate (function that allows to give code)
#create new function spherical coordinate
class Point:
    def __init__(self, coordinate: list[float]):
        self.cooridnate = coordinate

c = Point([1,2,3])
print(c.cooridnate)
d= Point([3,4,5])
print(d.cooridnate)