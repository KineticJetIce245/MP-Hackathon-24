from Point import Point
a = [Point([1, 1, 0]), Point([1, 2, 0]), Point([1, 5, 0]), Point([1, 9, 0])]
a.sort(key = lambda a: a.coordinates["x"])
for i in a:
    print(i)