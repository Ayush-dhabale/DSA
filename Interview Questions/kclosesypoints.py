#A array of points in given, return k points which are closest to the origin

from heapq import heappush, heappop
import math
def getDist(x,y):
    return math.sqrt(x*x + y*y)
    
def kClosestPoints(array,k):
    heap = []
    
    for point in array:
        x = point[0]
        y = point[1]
        
        heappush(heap,(getDist(x,y), point))
        
    result = []
    for i in range(k):
        result.append(heappop(heap)[1])
        
    return result

array = [[3,3],[5,-1],[-2,4]]
k = 2

result = kClosestPoints(array, k)
print(result)
        
        
    