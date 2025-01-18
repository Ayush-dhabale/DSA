#Reccurence relation : T(m-p) + n or T(q-m) + n

def partition(array,p,q):
    i = p
    pivot = array[p]
    
    for j in range(i+1,q+1):
        if array[j] < pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
            
    array[i],array[p] = array[p],array[i]
    
    return i

def selectionProcedure(array,p,q,k):
    m = partition(array,p,q)
    
    if m == k - 1:
        return array[m]
    
    elif m > k - 1 :
        return selectionProcedure(array,p,m-1,k)
    
    else:
        return selectionProcedure(array,m + 1 ,q,k)

array = [70,50,27,99,85,47,123,34,147]
# [27,34,47,50,70,85,99,123,147]

result =selectionProcedure(array,0,len(array) - 1,4)
print(result)