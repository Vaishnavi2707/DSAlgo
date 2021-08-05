# Time : O(n)
# Space : O(1)
# Function to reverse arr[] from index start to end
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        print("temp = %d , arr[start] = %d , arr[end] = %d " %(temp,arr[start],arr[end]))

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
    for i in range(0, n):
        print(arr[i])

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

