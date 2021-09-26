

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
    string = input("Enter String : ")  
    s = Stack(len(string))         
    for i in string:
        s.push(i)
    print("Reversed String : ", end = "")
    for i in range(len(string)):
        print(s.pop(),end = "")
    










