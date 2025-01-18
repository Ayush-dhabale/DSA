#Inversions i < j and arr[i] > arr[j]  ...(basically swaps required)
def mergeCount(array,lower,upper,mid):
    i, j = lower , mid + 1
    temp = []
    inv_count = 0
    
    while i <= mid and j <= upper:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
            
        else:
            temp.append(array[j])
            inv_count += (mid - i + 1)
            j += 1
            
    while i<= mid:
        temp.append(array[i])
        i += 1
        
    while j <= upper:
        temp.append(array[j])
        j += 1
        
    for i in range(len(temp)):
        array[lower + i] = temp[i]
        
    return inv_count


def mergeSort(array,lower,upper):
    inv_count = 0
    if lower < upper:
        mid = lower + (upper - lower) // 2
        
        inv_count += mergeSort(array,lower,mid)
        inv_count += mergeSort(array,mid + 1, upper)
        inv_count += mergeCount(array,lower,upper,mid)
        
    return inv_count


array = [50,70,45,5,79,47,29,52]

result = mergeSort(array,0,len(array) - 1)
print(result)