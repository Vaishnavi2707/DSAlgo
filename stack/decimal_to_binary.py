
"""Stack using array using top"""
class Stack:
    def __init__(self,mx = 100):
        self.stack = []
        self.mx = mx
        self.top = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])
    
    def isEmpty(self):
        if(self.top <= 0):
            return True
        else:
            return False

    def isFull(self):
        if(self.top >= self.mx):
            return True
        else:
            return False

    def push(self,data):
        if(self.isFull()):
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.top += 1

    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow")
        else:
            n = self.stack.pop()
            self.top -= 1
            return n
        
    def peek(self):
        if(self.isEmpty()):
            print("Stack Empty")
        else:
            ele = self.stack[self.top]
            return ele

    def size(self):
        return self.top

    
    def dtob(self,decimal, base = 2):
        while decimal > 0:
            myStack.push(decimal % base)
            decimal //= base

        result = ''
        while not myStack.isEmpty():
            result += str(myStack.pop())

        return result

if __name__ == "__main__":
    stack = Stack()
    num = int(input("Enter Number to convert decimal to binary : "))
    dec = dtob(num)
    print(dec)



