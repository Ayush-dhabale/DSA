#We have three colors as Red = 0, Green = 1, Blue = 2
#Now array of colors is given, we have sort the color

#approach 1
#Using sorting algorithm 
#TC : O(nlog(n))
#SC : O(1)


#Approach 2 (Two pointers)
#TC : O(n)
#SC : O(1)

def sortColors(array):
    current = p0 = 0
    p2 = len(array) - 1
    
    while p2 >= current:
        if array[current] == 0:
            array[current], array[p0] = array[p0],array[current]
            p0 += 1
            current += 1
            
        elif array[current] == 2:
            array[current], array[p2] = array[p2], array[current]
            p2 -= 1
            
        else:
            current += 1
            
    return array

array = [2,1,0,2,1,1,2,2,0,0]
print(sortColors(array))