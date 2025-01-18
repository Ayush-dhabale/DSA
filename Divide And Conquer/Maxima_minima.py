#TC : O(n)
#Recurrence Relation : 2T(n/2) + c

def maximaMinima(array,lower,upper):
    if upper == lower:
        max_ = array[lower]
        min_ = array[lower]
    
    elif lower + 1 == upper:
        if array[lower] > array[upper]:
            max_ = array[lower]
            min_ = array[upper]
        
        else:
            max_ = array[upper]
            min_ = array[lower]
    
    else:
        mid = (upper + lower) // 2
        
        maxR, minR = maximaMinima(array,mid + 1 , upper)
        maxL, minL = maximaMinima(array,lower,mid)
        
        if maxR > maxL:
            max_ = maxR
        else:
            max_ = maxL
        
        if minR < minL:
            min_ = minR
        
        else:
            min_ = minL
        
    return max_ , min_

array = [23,1,3,4,79,2,3,0,100000,-12222]

i,j = maximaMinima(array,0,9)
print(i,j)
        
    
        
        
    