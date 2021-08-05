#Right rotate / cyclically rotate an array by one / anticlockwise rotation

"""Method 1 """
#Time : O(n)    Space :O(1)
# Method for rotation
def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];

    arr[0] = x;


# Driver function
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ')


'''
O/P
Given array is
1 2 3 4 5 
Rotated array is
5 1 2 3 4 
Process finished with exit code 0




'''