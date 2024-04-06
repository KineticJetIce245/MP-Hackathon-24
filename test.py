from PointCloud import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point_list = list()
for i in range(30):
    x = (random.random()-0.5)*10
    y = (random.random()-0.5)*10
    z = (random.random()-0.5)*10
    point_list.append(Point([x,y,z]))

s = PointStage(point_list)
lps = s.loopdify()
for lp in lps:
    print(lp)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for lp in lps:
    x,y,z = [],[],[]
    for pt in lp.point_list:
        x.append(pt.coordinates['x'])
        y.append(pt.coordinates['y'])
        z.append(pt.coordinates['z'])
    x.append(lp.point_list[0].coordinates['x'])
    y.append(lp.point_list[0].coordinates['y'])
    z.append(lp.point_list[0].coordinates['z'])
    ax.scatter(x,y,z, c='r',s=100)
    ax.plot(x,y,z, color='r')
plt.show()