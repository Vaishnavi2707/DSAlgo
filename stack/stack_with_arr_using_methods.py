
#Time : O(1)
#Pros: Easy to implement. Memory is saved as pointers are not involved. 
#Cons: It is not dynamic. It doesn’t grow and shrink depending on needs at runtime.

# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize

# Function to create a stack. It initializes size of stack as 0
def createStack():
	stack = []
	return stack

# Stack is empty when stack size is 0
def isEmpty(stack):
	return len(stack) == 0

# Function to add an item to stack. It increases size by 1
def push(stack, item):
	stack.append(item)
	print(item + " pushed to stack ")
	
# Function to remove an item from stack. It decreases size by 1
def pop(stack):
	if (isEmpty(stack)):
		return str(-maxsize -1) # return minus infinite
	
	return stack.pop()

# Function to return the top from stack without removing it
def peek(stack):
	if (isEmpty(stack)):
		return str(-maxsize -1) # return minus infinite
	return stack[len(stack) - 1]

# Driver program to test above functions
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")


"""
op
10 pushed into stack
20 pushed into stack
30 pushed into stack
30 Popped from stack
Top element is : 20
Elements present in stack : 20 10 
"""
