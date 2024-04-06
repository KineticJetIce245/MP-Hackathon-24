
#class with coordinate attributes , initialize with coordinates,
#give coordinate (function that allows to give code)
#put it into one dictionnary
import math

class Point:
    def __init__(self, coordinate: list[float]) -> None:
        self.coordinates = {"x": coordinate[0], "y": coordinate[1], "z": coordinate[2]}
        self.coordinates.update(self.__calculate_sph_coordinate())
       
        
    

    def __calculate_sph_coordinate(self) -> dict:
        x = self.coordinates["x"]
        y = self.coordinates["y"]
        z = self.coordinates["z"]
        r = math.sqrt(x**2 + y**2 + z**2)
        r2d = math.sqrt(x**2 + y**2)
        theta = math.atan2(y,x)
        if z == 0:
            phi = 0
        elif z > 0:
            if r2d == 0:
                phi = math.pi/2
            else:
                phi = math.atan(z/r2d)
        else:
            phi = math.atan(z/r2d)
        return {'r': r, 'theta': theta, 'phi': phi}



# on top how to visualize the different "exceptional cases" that could happen --> making sure it works
#create new function spherical coordinate
# x= radius (Euclidean distance --> pythagore)
# x >= 0

# y= polar angle 
#0<= y <= pi rad

#z= azimuth
#0 <= z < 2pi rad

#c = Point([1,2,3])
#print(c.coordinate["x"])
d= Point([0,0,0])
print(d.coordinates)

