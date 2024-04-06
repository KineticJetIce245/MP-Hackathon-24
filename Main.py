from PointCloud import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# a set of points

s = PointStage([
    Point([1,3,3]),
    Point([1,3,3]),
    Point([1,3,3]),
    Point([1,3,3]),
    Point([1,3,3]),
    Point([1,3,3]),
    Point([1,3,3]),
])


plt.figure('SPLTV',figsize=(10,5))
custom=plt.subplot(121,projection='3d')

for lp in s.loops_list:
    x,y,z = [],[],[]
    for pt in lp.point_list:
        x.append(pt.coordinates['x'])
        y.append(pt.coordinates['y'])
        z.append(pt.coordinates['z'])
    x.append(lp.point_list[0].coordinates['x'])
    y.append(lp.point_list[0].coordinates['y'])
    z.append(lp.point_list[0].coordinates['z'])
    custom.scatter(x,y,z, c='r',s=100)
    custom.plot(x,y,z, color='r')
    x,y,z = [],[],[]
    x.append(lp.center_of_mass.coordinates['x'])
    y.append(lp.center_of_mass.coordinates['y'])
    z.append(lp.center_of_mass.coordinates['z'])
    custom.scatter(x,y,z, c='g',s=100)
    

for tri in s.mesh_list:
    #x-2y+z=6
    x1=tri.give_eu_cord_scatter()[0]
    y1=tri.give_eu_cord_scatter()[1]
    z1=tri.give_eu_cord_scatter()[2]  # z1 should have 3 coordinates, right?
    custom.scatter(x1,y1,z1)

    # 1. create vertices from points
    verts = [list(zip(x1, y1, z1))]
    # 2. create 3d polygons and specify parameters
    srf = Poly3DCollection(verts, alpha=.25, facecolor='#800000')
    # 3. add polygon to the figure (current axes)
    plt.gca().add_collection3d(srf)

plt.show()