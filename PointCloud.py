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

class Triangle:
    def __init__(self, vertexes: list[Point]) -> None:
        self.vertexes = vertexes

    # [x1, x2, x3], [y1, y2, y3], [z1, z2, z3]
    def give_eu_cord_scatter(self) -> list[list]:
        return [
            [self.vertexes[0].coordinates['x'], self.vertexes[1].coordinates['x'], self.vertexes[2].coordinates['x']],
            [self.vertexes[0].coordinates['y'], self.vertexes[1].coordinates['y'], self.vertexes[2].coordinates['y']],
            [self.vertexes[0].coordinates['z'], self.vertexes[1].coordinates['z'], self.vertexes[2].coordinates['z']]
                ]

class PointLoop:
    def __init__(self, loop: list[Point]) -> None:
        self.point_list = loop
        x,y,z = 0,0,0
        total_num = len(self.point_list)
        for pt in self.point_list:
            x += pt.coordinates['x']
            y += pt.coordinates['y']
            z += pt.coordinates['z']
        self.center_of_mass = Point([x/total_num, y/total_num, z/total_num])
        self.ref_list = list[tuple]()
        for pt in self.point_list:
            self.ref_list.append((pt, self.center_of_mass.ref_cord(pt)))
        self.__close()
           
    def __str__(self) -> str:
        ret_val = '['
        for k in self.point_list:
            ret_val += k.__str__() + ';'
        return ret_val

    # Close up the loops
    def __close(self) -> None:
        self.ref_list.sort(key = lambda a: (a[1].coordinates['theta'], a[1].coordinates['r'], a[1].coordinates['phi']))
        re_org_list = list[Point]()
        
        for tp in self.ref_list:
            re_org_list.append(tp[0])
        
        self.point_list = re_org_list
    
    def connect_loop(self, point_loop: 'PointLoop') -> list[Triangle]:
        srf = self.ref_list
        prf = point_loop.ref_list
        tri_list = list[Triangle]()
        
        o_sum = 0
        # self to point_loop
        n = len(srf)
        for i in range(n):
            j = (i + 1) % n
            angle_range = [srf[i][1].coordinates['theta'], srf[j][1].coordinates['theta']]
            should_translate = False
            if angle_range[0] > angle_range[1]:
                should_translate = True
            m = len(prf)
            sati_points = list[Point]()
            for k in range(m):
                pt = prf[k][1]
                p_theta = pt.coordinates['theta']
                if (should_translate):
                    if angle_range[1] >= p_theta >= -math.pi*2 or math.pi*2 >= p_theta >= angle_range[0]:
                        sati_points.append(prf[k][0]) # With original coordinate
                    continue
                if angle_range[0] <= p_theta and p_theta < angle_range[1]:
                    sati_points.append(prf[k][0]) # With original coordinate
            o = len(sati_points)
            o_sum += o
            if o == 0: continue
            if o == 1:
                tri_list.append(Triangle([sati_points[0], srf[i][0], srf[j][0]]))
                continue
            if o == 2:
                tri_list.append(Triangle([sati_points[1], srf[i][0], srf[j][0]]))
                tri_list.append(Triangle([sati_points[0], sati_points[1], srf[i][0]]))
                continue
            for k in range(o - 1):
                tri_list.append(Triangle([sati_points[k], sati_points[k+1], srf[i][0]]))
            tri_list.append(Triangle([sati_points[o-1], srf[j][0], srf[i][0]]))
            
            '''
            # 0, 1, 2, 3, 4, 5, 6 -> 0, 1, 2, 3 to first point; 3, 4, 5, 6 to the second
            if o % 2 == 1:
                half_o = int(o / 2)
                for k in range(half_o-1):
                    tri_list.append(Triangle([sati_points[k], sati_points[k+1], srf[i][0]]))
                    tri_list.append(Triangle([sati_points[k+half_o], sati_points[k+half_o+1], srf[j][0]]))
            else:
                half_o = o/2
                for k in range(o-1):
                    if k < half_o-1:
                        tri_list.append(Triangle([sati_points[k], sati_points[k+1], srf[i][0]]))
                    else:
                        tri_list.append(Triangle([sati_points[k], sati_points[k+1], srf[j][0]]))
            '''
            
        # point loop to self
        n = len(prf)
        for i in range(n):
            j = (i + 1) % n
            angle_range = [prf[i][1].coordinates['theta'], prf[j][1].coordinates['theta']]
            should_translate = False
            if angle_range[0] > angle_range[1]:
                should_translate = True
            m = len(srf)
            sati_points = list[Point]()
            for k in range(m):
                pt = srf[k][1]
                p_theta = pt.coordinates['theta']
                if (should_translate):
                    if angle_range[1] >= p_theta >= -math.pi*2 or math.pi*2 >= p_theta >= angle_range[0]:
                        sati_points.append(srf[k][0]) # With original coordinate
                    continue
                if angle_range[0] <= p_theta and p_theta < angle_range[1]:
                    sati_points.append(srf[k][0]) # With original coordinate
                    
            o = len(sati_points)
            o_sum += o
            if o == 0: continue
            if o == 1:
                tri_list.append(Triangle([sati_points[0], prf[i][0], prf[j][0]]))
            if o == 2:
                tri_list.append(Triangle([sati_points[1], prf[i][0], prf[j][0]]))
                tri_list.append(Triangle([sati_points[0], sati_points[1], prf[i][0]]))
            
            for k in range(o - 1):
                tri_list.append(Triangle([sati_points[k], sati_points[k+1], srf[i][0]]))
            tri_list.append(Triangle([sati_points[o-1], srf[j][0], srf[i][0]]))
            '''
            # 0, 1, 2, 3, 4, 5, 6 -> 0, 1, 2, 3 to first point; 3, 4, 5, 6 to the second
            if o % 2 == 1:
                half_o = int(o / 2)
                for k in range(half_o-1):
                    tri_list.append(Triangle([sati_points[k], sati_points[k+1], prf[i][0]]))
                    tri_list.append(Triangle([sati_points[k+half_o], sati_points[k+half_o+1], prf[j][0]]))
            else:
                half_o = o/2
                for k in range(o-1):
                    if k < half_o-1:
                        tri_list.append(Triangle([sati_points[k], sati_points[k+1], prf[i][0]]))
                    else:
                        tri_list.append(Triangle([sati_points[k], sati_points[k+1], prf[j][0]]))
            '''
        print(len(tri_list))
        return tri_list
    
        
# Point Clouds
class PointStage:
    # Initiate with an array of points
    def __init__(self, point_cloud: list[Point]) -> None:
        self.point_cloud = point_cloud
        point_cloud.sort(key = lambda p: p.coordinates['z'])
        self.loops_list = self.__loopdify()
        self.mesh_list = self.__create_mesh()
    
    def __loopdify(self) -> list[PointLoop]:
        loops = list[PointLoop]()
        pl = self.point_cloud
        current_z = pl[0].coordinates['z']
        
        i = 0
        loop = list[Point]()
        do_continue_adding = False
        for pt in pl:
            pz = pt.coordinates['z']
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
            if (i < 3):
                i += 1
                loop.append(pt)
            else:
                loop.append(pt)
                i = 0
                current_z = pz
                do_continue_adding = True
        
        loops.append(PointLoop(loop))
        return (loops)

    def __create_mesh(self) -> list[Triangle]:
        n = len(self.loops_list)
        all_triangle = list[Triangle]()
        for i in range(n-1):
            print(self.loops_list)
            print(1)
            all_triangle.extend((self.loops_list[i].connect_loop(self.loops_list[i+1])))
        m = len(self.loops_list[0].point_list)
        for i in range(m):
            pt1 = self.loops_list[0].point_list[i]
            pt2 = self.loops_list[0].point_list[(i+1)%m]
            all_triangle.append(Triangle([self.loops_list[0].center_of_mass, pt1, pt2]))
        o = len(self.loops_list[-1].point_list)
        for i in range(o):
            pt1 = self.loops_list[-1].point_list[i]
            pt2 = self.loops_list[-1].point_list[(i+1)%o]
            all_triangle.append(Triangle([self.loops_list[-1].center_of_mass, pt1, pt2]))
        return all_triangle
    # Divide the point clouds to loops
    # Deprecated method
    def __deprecated_loopdify(self) -> list[PointLoop]:
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
        