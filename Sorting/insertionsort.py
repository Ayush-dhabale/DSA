#best case O(n) comparisions = n - 1, swaps = 0
#Worst case O(n^2) camparisions = n(n-1) / 2, swaps = n(n-1) / 2

#Preffered if the array is almost sorted
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j] = key
        
    return arr
            