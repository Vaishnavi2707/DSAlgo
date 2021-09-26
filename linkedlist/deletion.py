class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    #insert at beginning
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self , key):
        temp = self.head
        #if key is at head node
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        #if key is at another position
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        #if key is not in LL
        if(temp == None):
            print("Key not present")
            return
        #remove link of node from ll
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data , end = " ")
            temp = temp.next

if __name__ == "__main__":
    l = LinkedList()
    l.push(5)
    l.push(6)
    l.push(7)
    l.push(8)
    l.push(9)
    print("Created List : ",end = " ")
    l.printList()
    l.deleteNode(7)
    print(" List : ",end = " ")
    l.printList()
