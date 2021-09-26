class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
#Add node at begining
    def pushAtBeg(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#Add node after a given node
    def pushAfter(self,prev_node , new_data):
        if(prev_node is None):
            print("Given Previous node must be in list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

#Add node at end
    def pushAtEnd(self, new_data):
        new_node = Node(new_data)
        #if ll is empty, make newnode as 
        if(self.head is None):
            self.head = new_node
            return
        #else traverse till last node
        last = self.head
        while(last.next):
            last = last.next
        #change the next of last node
        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":
    l = LinkedList()
    l.pushAtBeg(5)
    l.pushAtBeg(4)
    l.pushAfter(l.head,6)
    l.pushAtEnd(7)
    l.pushAfter(l.head.next , 0)
    print("Linked List :")
    l.printList()
    
        
