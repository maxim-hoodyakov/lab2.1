import math
x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
pol = (a + b + c) / 2
s = math.sqrt(pol * (pol - a) * (pol - b) * (pol - c))
perimeter = a + b + c
print("Периметр треугольника:", perimeter)
print("Площадь треугольника:", s)