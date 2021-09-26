#Shift zeros to end

    
def shiftZerosToEnd(arr):
    l =len(arr)
    count = 0
    for i in range(l):
        if(arr[i]!=0):
            arr[count] = arr[i]
            count+=1
    while(count<l):
        arr[count] = 0
        count+=1
    return arr
        

#driver code
arr = list(map(int,input("Enter array : ").split()))
shiftZerosToEnd(arr)
for i in arr:
    print(i,end = " ")
