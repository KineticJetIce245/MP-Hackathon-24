from PointCloud import *
import random

point_list = list[Point]()
for i in range(10):
    x = (random.random()-0.5)*10
    y = (random.random()-0.5)*10
    z = (random.random()-0.5)*10
    point_list.append(Point([x,y,z]))

for i in point_list:
    x = round(i.coordinates['x'],2)
    y = round(i.coordinates['y'],2)
    z = round(i.coordinates['z'],2)
    r = round(i.coordinates['r'],2)
    t = round(i.coordinates['theta'],2)
    p = round(i.coordinates['phi'],2)
    print('['+str(x)+','+str(y)+','+str(z)+';'+str(r)+','+str(t)+','+str(p)+']')