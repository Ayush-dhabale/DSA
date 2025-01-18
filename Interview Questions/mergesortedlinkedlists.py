class Node:
    def __init__(self,data = 0, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def merge(self,head1,head2):
        temp = None
        if not head1:
            return head2
        
        if not head2:
            return head1
        
        if head1.data <= head2.data:
            temp = head1
            temp.next = self.merge(head1.next,head2)
            
        else:
            temp = head2
            temp.next = self.merge(head1,head2.next)
        
        return temp            