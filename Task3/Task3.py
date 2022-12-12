import math
userX1 = int(input("enter X1:"))
userY1 = int(input("enter Y1:"))
userX2 = int(input("enter X2:"))
userY2 = int(input("enter Y2:"))

def DistanceBetweenTwoPoints(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    print(round(distance, 3))

DistanceBetweenTwoPoints(userX1, userY1, userX2, userY2)