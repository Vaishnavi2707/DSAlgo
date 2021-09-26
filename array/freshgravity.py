
def processArray(arr):
    for i in range(len(arr)):
        if(arr[i]%11 == 0 and arr[i]%5 == 0):
            arr[i]= -3
        elif(arr[i]%11 == 0):
            arr[i] = -2
        elif(arr[i]%5 == 0):
            arr[i] = -1
        else:
            continue
    return arr


if __name__ == "__main__":
    arr = []
    print("input")
    while(True):
        e = int(input())
        if(e<0):
            break
        arr.append(e)
    processArray(arr)
    print("onput")
    for i in range(len(arr)):
        print(arr[i])
        
