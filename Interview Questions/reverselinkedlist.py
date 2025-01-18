class Node:
    def __init__(self,data = 0, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
        
    def reverseList(self):
        prev_node = next_node = None
        temp = self.head
        
        while temp:
            next_node = temp.next
            temp.next = prev_node
            prev_node = temp
            temp = temp.next
            
        self.head = temp
        