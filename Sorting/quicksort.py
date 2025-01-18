
def partition(array,p,q):
    i = p
    pivot = array[p]
    
    for j in range(i+1,q+1):
        if array[j] < pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
            
    array[i],array[p] = array[p],array[i]
    
    return i

def qucikSort(array,p,q):
    if p < q:
        mid = partition(array,p,q)
        qucikSort(array,p,mid - 1)
        qucikSort(array,mid+1,q)
        
    return array

array = [70,50,27,99,85,47,123,34,147]

result = qucikSort(array,0,len(array) - 1)
print(result)