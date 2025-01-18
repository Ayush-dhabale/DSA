class Node:
     def __init__(self,data):
         self.data = data
         self.next = None
         
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    #Insert at the begining
    def insertAtBegining(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    #Insert in between (with value)
    def insertInBetween1(self,new_data,previous_data):
        
        previous_node = self.head
        
        while previous_node.data != previous_data:
            previous_node = previous_node.next
            
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
        
    #Insert in between (with node)
    def insertInBetween2(self,new_data,previous_node):
        if previous_node:
            new_node = Node(new_data)
            new_node.next = previous_node.next
            previous_node.next = new_node
        else:
            self.insertAtLast(new_data) 
    
    #Insert at last
    def insertAtLast(self,new_data):
        
        if self.head:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            
            new_node = Node(new_data)
            last_node.next = new_node
            
        else:
            self.insertAtBegining(new_data)
            
    #Print Linked List
    def printList(self):
        temp = self.head
        
        while temp:
            print(str(temp.data)+"  ",end=" ")
            temp = temp.next
            
lList = LinkedList()

lList.insertAtLast(120)
lList.insertAtBegining(12)
lList.insertAtBegining(24)
lList.insertAtBegining(36)
lList.insertAtBegining(48)
lList.insertAtBegining(60)
lList.insertAtBegining(72)
lList.insertInBetween1(67,36)
lList.insertInBetween1(97,60)
lList.insertInBetween2(107,lList.head.next)
lList.insertAtLast(10)
lList.printList()