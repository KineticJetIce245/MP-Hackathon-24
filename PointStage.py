from Point import Point
from PointLoop import PointLoop
import random
# Point Clouds
class PointStage:
    # Initiate with an array of points
    def __init__(self, point_cloud: list[Point]) -> None:
        self.point_cloud = point_cloud
        point_cloud.sort(key = lambda p: p.coordinates["z"])
        
    # Divide the point clouds to loops
    def loopdify(self) -> list[PointLoop]:
        loops = list[PointLoop]()
        pl = self.point_cloud
        first_point = pl[0]
        last_point = pl[-1]

        last_z = last_point.coordinates["z"]
        current_z = first_point.coordinates["z"]
        
        i = 0
        starting_index = 0
        
        first_loop = list[Point]()
        last_loop = list[Point]()
        
        # First Points
        for pt in pl:
            pz = pt.coordinates["z"]
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
            pz = pt.coordinates["z"]
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
                
                if (i < 2):
                    i += 1
                    loop.append(pt)
                else:
                    loop.append(pt)
                    i == 0
                    current_z = pz
                    do_continue_adding = True
            else:
                last_loop.append(pt)
        
        loops.append(PointLoop(loop))
        loops.append(PointLoop(last_loop))
        return (loops)

test_list = [
    Point([-1, 3, 4]),
    Point([-1, 2, 8]),
    Point([0, 3, 8]),
    Point([1, 2, 0]),
    Point([3, 5, 2]),
    Point([2, 2, 5]),
    Point([4, 2, 4]),
    Point([3, 7, 4]),
    Point([4, 3, 4]),
]      
s = PointStage(test_list)
for i in s.loopdify():
    print(i)
    