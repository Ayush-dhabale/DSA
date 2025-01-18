#TC : O(nlog(n))

class Heap:
    def __init__(self,array) :
        self.heap = array
        
        
    def heapifyDown(self,n,parent):
        smallest = parent
        left = 2 * parent + 1
        right = 2 * parent + 2
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
            
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != parent:
            self.heap[parent] , self.heap[smallest] =  self.heap[smallest] , self.heap[parent] 
            self.heapifyDown(n,smallest)
            
    def heapifyUp(self,child):
        parent = (child - 1) // 2
        
        if child > 0 and self.heap[child] < self.heap[parent]:
            self.heap[parent] , self.heap[child] = self.heap[child] , self.heap[parent]
            self.heapifyUp(parent)
            
    def minHeap(self):
        for i in range(len(self.heap) // 2 - 1, -1 , -1):
            self.heapifyDown(len(self.heap),i)
            
    def insert(self,element):
        self.heap.append(element)
        self.heapifyUp(len(self.heap) - 1)
        
    def delete(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(len(self.heap),0)
        return root
    
    
def heapSort(array):
    heap_obj = Heap(array)
    heap_obj.minHeap()
    print(array)
    for i in range(len(array) - 1, 0 , -1):
        array[i] , array[0] = array[0], array[i]
        heap_obj.heapifyDown(i,0)
    
    array.reverse() 
    print(array)   
    #return array

#DriverCode
array = [8,3,4,1,5,2,6,9,7]
#result = heapSort(array)
heapSort(array)
        