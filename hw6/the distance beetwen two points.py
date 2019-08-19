from math import *
def distance(x1, y1, x2, y2):
    dis=sqrt((x1-x2)**2+(y1-y2)**2)
    return float('{:.2f}'.format(dis))