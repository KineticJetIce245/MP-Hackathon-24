from PointCloud import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # appropriate import to draw 3d polygons
# Random number set just run the file

point_list = list()

for i in range(14):
    x = (random.random()-0.5)*5
    y = (random.random()-0.5)*5
    z = 1+(random.random()-0.5)+i/5
    point_list.append(Point([x,y,z]))

s = PointStage(point_list)
mesh = list()
for tri in s.mesh_list:
    mesh.append(tri.give_eu_cord())
print("Total Area:" + str(Area_pointcloud.calculate_mesh_area(mesh)))

plt.figure('SPLTV',figsize=(10,5))
custom=plt.subplot(111,projection='3d')

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