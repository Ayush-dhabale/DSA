class Node:
    def __init__(self,data=0,next=None):
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Searching
    def search(self,value):
        temp = self.head
        
        while temp:
            if temp.data == value:
                return True
            
            temp = temp.next
        return False
    
    