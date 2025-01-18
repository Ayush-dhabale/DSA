#There points are given, tell whether they are collinear or not
#Approach one - slopes (y2 - y1)(x3-x2) = (y3-y2)(x2-x1)
#Approach Two - Area of triangle 1/2(x1 * (y2-y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#O(1)


#1
def Iscollinear(x1,x2,x3,y1,y2,y3):
    if (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1):
        return True
    
    return False
#2
def Iscollinear(x1,x2,x3,y1,y2,y3):
    if 0.5 * (x1*(y2-y3) + x2 * (y3-y2) + x3 * (y1 - y2)):
        return True
    
    return False

