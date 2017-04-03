import math
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
x = int(input("X1"))
y = int(input("Y1"))
xx= int(input("X2"))
yy= int(input("Y2"))
print(distance(x,y,xx,yy))
