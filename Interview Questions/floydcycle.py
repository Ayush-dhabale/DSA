class Node:
    def __init__(self,data = 0, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def cycleDetection(self):
        slow = self.head
        fast = self.head
        
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                return True
        return False