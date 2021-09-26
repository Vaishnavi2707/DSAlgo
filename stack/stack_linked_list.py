
# stack implementation using a linked list.
# node class
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
 
class Stack:
   def __init__(self):
      self.head = Node("head")
      self.size = 0
 
   def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.value) + "->"
         cur = cur.next
      return out[:-3]  
 
   def getSize(self):
      return self.size
    
   def isEmpty(self):
      return self.size == 0
    
   def peek(self):
      if self.isEmpty():
         raise Exception("Peeking from an empty stack")
      return self.head.next.value
 
   def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      self.size += 1
      
   def pop(self):
      if self.isEmpty():
         raise Exception("Popping from an empty stack")
      remove = self.head.next
      self.head.next = self.head.next.next
      self.size -= 1
      return remove.value
 
if __name__ == "__main__":

    mx = int(input("Enter size :"))
    s = Stack(mx)
    lst = list(map(int,input("Enter Stack :").split()))
    print("Pushing : ")           
    for i in lst:
        s.push(i)
    print("list : " , lst)
    print("stack : " , s)
    size = s.size()
    print("Size of stack : ",size)
    print("Poping : ")
    for i in range(size-3):
        print(s.pop(), end = " ")
    print("stack : " , s)
    print("Peek :" ,s.peek())
    print("stack : " , s)



