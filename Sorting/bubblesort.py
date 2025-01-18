# Comparisions = n(n-1)/2
#Swaps = n(n-1)/2
#TC : o(n^2)
# last element is the first sorted elememt

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr


arr = [70,20,50,30,90,5,15]

print(bubbleSort(arr))