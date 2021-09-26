# rearrange an sorted array in minimum maximum form

def rearrange(arr, n):
    res=[0 for i in range(n)]
    max = n - 1
    min = 0

    for i in range(n):
        if i % 2 == 0:
            res[i] = arr[max]
            max -= 1

        else:
            res[i] = arr[min]
            min += 1

    for i in range(n):
        arr[i]=res[i]

    return arr

# Driver code
arr = list(map(int,input("Enter array : ").split()))
n = len(arr)
print("Origianl Array")
for i in range(n):
    print(arr[i], end=" ")

rearrange(arr, n)
print("\nModified Array")
for i in range(n):
    print(arr[i], end=" ")

