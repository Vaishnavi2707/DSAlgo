
"""Stack using array"""
class Stack:
    def __init__(self,mx):
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
    for i in range(size):
        print(s.pop(), end = " ")
    print("Peek :" ,s.peek())





