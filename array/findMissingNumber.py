




def findMissing(arr):
    l = len(arr)
    if(arr[0]==0):
        n=l
    else:
        n=l+1
    expectedSum = n*(n+1)/2
    arrSum = 0
    for i in range(l):
        arrSum = arrSum + arr[i]
    missingNum = expectedSum - arrSum
    return int(missingNum)



if __name__ == '__main__':
    myArray = list(map(int,input("Enter Array : ").split()))
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray))










"""
def findMissing(myArray, n):
    n = n - 1
    totalSum = (n * (n + 1)) // 2
    for i in range(0, n):
        totalSum -= myArray[i]

    return totalSum

if __name__ == '__main__':
    myArray = list(map(int,input("Enter Array : ").split()))
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray, len(myArray)))
"""
