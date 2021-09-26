

"""Stack using array"""
class Stack:
    def __init__(self,mx):
        self.stack = []
        self.mx = mx

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])
    
    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False

    def isFull(self):
        if(len(self.stack)>= self.mx):
            return True
        else:
            return False

    def push(self,data):
        if(self.isFull()):
            print("Stack Overflow")
        else:
            self.stack.append(data)

    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow")
        else:
            n = self.stack.pop()
            return n
    def peek(self):
        return self.stack[-1]
        
        

if __name__ == "__main__":
    mx = int(input("Enter size :"))
    s = Stack(mx)
    lst = list(map(int,input("Enter Stack :").split()))
    print("Pushing : ")           
    for i in lst:
        s.push(i)
    print("list : " , lst)
    print("stack : " , s)
    print("Poping : ")
    for i in range(2):
        print(s.pop())
    
    print("Peek :" ,s.peek())







"""
# Python program to demonstrate
# stack implementation using a linked list.
# node class
class Node:
   def __init__(self, value):
      self.value = value
      self.next = None
 
class Stack:
    
   # Initializing a stack.
   # Use a dummy node, which is
   # easier for handling edge cases.
   def __init__(self):
      self.head = Node("head")
      self.size = 0
 
   # String representation of the stack
   def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.value) + "->"
         cur = cur.next
      return out[:-3]  
 
   # Get the current size of the stack
   def getSize(self):
      return self.size
    
   # Check if the stack is empty
   def isEmpty(self):
      return self.size == 0
    
   # Get the top item of the stack
   def peek(self):
       
      # Sanitary check to see if we
      # are peeking an empty stack.
      if self.isEmpty():
         raise Exception("Peeking from an empty stack")
      return self.head.next.value
 
   # Push a value into the stack.
   def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      self.size += 1
      
   # Remove a value from the stack and return.
   def pop(self):
      if self.isEmpty():
         raise Exception("Popping from an empty stack")
      remove = self.head.next
      self.head.next = self.head.next.next
      self.size -= 1
      return remove.value
 
# Driver Code
if __name__ == "__main__":
   stack = Stack()
   for i in range(1, 11):
      stack.push(i)
   print(f"Stack: {stack}")
 
   for _ in range(1, 6):
      remove = stack.pop()
      print(f"Pop: {remove}")
   print(f"Stack: {stack}")



"""





