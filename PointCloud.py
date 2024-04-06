import math
#class with coordinate attributes , initialize with coordinates,
#give coordinate (function that allows to give code)
#put it into one dictionnary
class Point:
    def __init__(self, coordinate: list[float]) -> None:
        self.coordinates = {'x': coordinate[0], 'y': coordinate[1], 'z': coordinate[2]}
        self.coordinates.update(self.__calculate_sph_coordinate())

    def __calculate_sph_coordinate(self) -> dict:
        x = self.coordinates['x']
        y = self.coordinates['y']
        z = self.coordinates['z']
        r = math.sqrt(x**2 + y**2 + z**2)
        r2d = math.sqrt(x**2 + y**2)
        theta = math.atan2(y,x)
        if z == 0:
            phi = 0
        else:
            if r2d == 0:
                phi = math.pi/2 if z > 0 else -math.pi/2
            else:
                phi = math.atan(z/r2d)
        return {'r': r, 'theta': theta, 'phi': phi}
    
    def __str__(self) -> str:
        return '(' + str(round(self.coordinates['x'], 3)) + ',' + str(round(self.coordinates['y'], 3)) + ',' + str(round(self.coordinates['z'], 3)) + ')'

    def ref_cord(self, p: 'Point') -> 'Point':
        x = p.coordinates['x'] - self.coordinates['x'] 
        y = p.coordinates['y'] - self.coordinates['y'] 
        z = p.coordinates['z'] - self.coordinates['z']
        return Point([x,y,z])


class PointLoop:
    def __init__(self, loop: list[Point]) -> None:
        self.point_list = loop
        self.__close()
           
    def __str__(self) -> str:
        ret_val = '['
        for k in self.point_list:
            ret_val += k.__str__() + ';'
        return ret_val

    # Close up the loops
    def __close(self) -> None:
        pl = self.point_list
        ref_list = list[tuple]()
        
        x,y,z = 0,0,0
        total_num = len(pl)
        for pt in pl:
            x += pt.coordinates['x']
            y += pt.coordinates['y']
            z += pt.coordinates['z']
        center_of_mass = Point([x/total_num, y/total_num, z/total_num])
        
        for pt in pl:
            ref_list.append((pt, center_of_mass.ref_cord(pt)))
        ref_list.sort(key = lambda a: (a[1].coordinates['theta'], a[1].coordinates['r'], a[1].coordinates['phi']))
        re_org_list = list[Point]()
        
        for tp in ref_list:
            re_org_list.append(tp[0])
        
        self.point_list = re_org_list
    
    #def connect_loop(self) -> list[Triangle]:
        
    
        
# Point Clouds
class PointStage:
    # Initiate with an array of points
    def __init__(self, point_cloud: list[Point]) -> None:
        self.point_cloud = point_cloud
        point_cloud.sort(key = lambda p: p.coordinates['z'])
        
    # Divide the point clouds to loops
    def loopdify(self) -> list[PointLoop]:
        loops = list[PointLoop]()
        pl = self.point_cloud
        first_point = pl[0]
        last_point = pl[-1]

        last_z = last_point.coordinates['z']
        current_z = first_point.coordinates['z']
        
        i = 0
        starting_index = 0
        
        first_loop = list[Point]()
        last_loop = list[Point]()
        
        # First Points
        for pt in pl:
            pz = pt.coordinates['z']
            if pz == current_z:
                first_loop.append(pt)
                i += 1
            else:
                starting_index = i
                break
        loops.append(PointLoop(first_loop))

        # Other points
        i = 0
        loop = list[Point]()
        do_continue_adding = False
        for pt in pl[starting_index::]:
            pz = pt.coordinates['z']
            if (pz != last_z):
                # Continue to add if having the same z
                if (do_continue_adding):
                    if (pz != current_z):
                        do_continue_adding = False
                        loops.append(PointLoop(loop))
                        loop = list[Point]()
                        loop.append(pt)
                        i += 1
                    else:
                        loop.append(pt)
                    continue
                
                # i + 1 points per loop
                if (i < 4):
                    i += 1
                    loop.append(pt)
                else:
                    loop.append(pt)
                    i = 0
                    current_z = pz
                    do_continue_adding = True
            else:
                last_loop.append(pt)
        
        loops.append(PointLoop(loop))
        loops.append(PointLoop(last_loop))
        return (loops)
    
class Triangle:
    def __init__(self, vertexes: list[Point]) -> None:
        self.vertexes = vertexes
        