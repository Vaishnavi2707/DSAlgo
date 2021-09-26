# Python Program to search an element
# in a sorted and pivoted array
"""METHOD 1 : Direct searching without finding pivot"""
#Time Complexity : O(log(n))        Space:O(1)

def search(arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid - 1, key)
        return search(arr, mid + 1, h, key)

    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid - 1, key)


# Driver program
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
i = search(arr, 0, len(arr) - 1, key)
if i != -1:
    print("Index: % d" % i)
else:
    print("Key not found")




"""METHOD 2: finding pivot then search"""
#Time Complexity : O(log(n))        Space:O(1)


def pivotedBinarySearch(arr, n, key):
    pivot = findPivot(arr, 0, n - 1);

    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n - 1, key);

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key);
    return binarySearch(arr, pivot + 1, n - 1, key);


def findPivot(arr, low, high):
    # base cases
    if high < low:
        return -1
    if high == low:
        return low

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)


# Standard Binary Search function*/
def binarySearch(arr, low, high, key):
    if high < low:
        return -1

    # low + (high - low)/2;
    mid = int((low + high) / 2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                            key);
    return binarySearch(arr, low, (mid - 1), key);


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ",
      pivotedBinarySearch(arr1, n, key))
