class Node:
    def __init__(self,data = 0 , next = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Deletion from begining
    def deleteFromBegining(self):
        if not self.head:
            print("There is no element to delete!!")
            return
        
        if self.head.next:
            self.head = self.head.next
        
        else:
            self.head = None
            
    #Delete from between
    def deleteFromBetween(self,node):
        if not self.head:
            print("There is no element to delete!!")
            return
        if node == self.head:
            self.deleteFromBegining()
            return
        
        
        temp = self.head
        while temp.next and temp.next != node:
            temp = temp.next
        
        if not temp.next:
            print("No such element present")
            return
        
        temp.next = node.next
        
    #DeleteFromLast
    def deleteFromLast(self):
        if not self.head:
            print("There is no element to delete!!")
            return
        if not self.head.next:
            self.deleteFromBegining()
        
        temp = self.head
        
        while temp.next.next:
            temp = temp.next
            
        temp.next = None
        
    #Print Linked List
    def printList(self):
        temp = self.head
        
        while temp:
            print(str(temp.data)+"  ",end=" ")
            temp = temp.next
        
first = Node(7)
second = Node(14)
third = Node(21)
fourth = Node(28)
fifth = Node(35)
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

lList = LinkedList()
lList.head = first


#Begining
lList.deleteFromBegining()
lList.printList()
print("\n\nbegining!!!!!!")

#last
lList.deleteFromLast()
lList.printList()
print("\n\nlast!!!!!!")

#Between
lList.deleteFromBetween(lList.head.next.next)
lList.printList()
print("\n\nBetween!!!!!!")

