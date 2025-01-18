#TC : O(nlog(n))
def merge(array,lower,upper,mid):
    left = array[lower : mid + 1]
    right = array[mid + 1 : upper + 1]
    
    i = j =  0
    k  = lower
    
    while i <  len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            
        else:
            array[k] = right[j]
            j += 1
            
        k += 1
        
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
        

def mergeSort(array,lower,upper):
    if upper > lower:
        mid = lower + (upper - lower) // 2

        mergeSort(array,lower,mid)
        mergeSort(array, mid + 1, upper)
        merge(array,lower,upper,mid)
    return array

array = [50,70,45,5,79,47,29,52]

result = mergeSort(array,0,len(array) - 1)
print(result)


    