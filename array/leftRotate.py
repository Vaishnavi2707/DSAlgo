# Left Rotate array by d elements / clockwise rotation

"""METHOD 2 : Reversal Algorithm"""

# Time : O(n)
# Space : O(1)
# Function to reverse arr[] from index start to end
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        #print("temp = %d , arr[start] = %d , arr[end] = %d " %(temp,arr[start],arr[end]))

        start += 1
        end = end - 1
# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is
    # greater than array length, then it will repeat so take only remainder i.e the extra nums
    d = d % n
    reverseArray(arr, 0, d - 1)
    reverseArray(arr, d, n - 1)
    reverseArray(arr, 0, n - 1)

def printArray(arr,n):
    print("rotated :")
    for i in range(0, n):
        print(arr[i],end = " ")

# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2

leftRotate(arr, d)
printArray(arr,n)



'''
O/P
temp = 1 , arr[start] = 2 , arr[end] = 1 
temp = 3 , arr[start] = 7 , arr[end] = 3 
temp = 4 , arr[start] = 6 , arr[end] = 4 
temp = 2 , arr[start] = 3 , arr[end] = 2 
temp = 1 , arr[start] = 4 , arr[end] = 1 
temp = 7 , arr[start] = 5 , arr[end] = 7 
3
4
5
6
7
1
2
'''



"""METHOD 1 : Left Rotate by 1"""
# Time : O(n*d)
# Space : O(1)
# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        # leftRotatebyOne(arr, n)
        temp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = temp


# Function to left Rotate arr[] of size n by 1*/
'''
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
'''
# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

'''
O/P
 3  4  5  6  7  1  2 
'''




"""METHOD 3 : using deque"""

# Time :O(n)    Space : O(1)
# Python3 implementation to print left
# rotation of any array K times
from collections import deque


# Function For The k Times Left Rotation
def leftRotate(arr, k, n):
    # The collections module has deque class
    # which provides the rotate(), which is
    # inbuilt function to allow rotation
    arr = deque(arr)

    arr.rotate(-k)
    arr = list(arr)
    print("arr rotated:")
    for i in range(n):
        print(arr[i], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    n = len(arr)
    k = 2

    # Function Call
    leftRotate(arr, k, n)
