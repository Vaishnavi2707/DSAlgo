import time
def getStarAndSuperStar(arr, n):
    # code here
    res = []
    max = arr[0]
    ind = 0
    for i in range(1, n):
        if (max > arr[i]):
            pass
        else:
            max = arr[i]
            ind = i
    k = ind + 1
    if (arr.count(max) > 1):
        res.append(-1)
    else:
        res.append(max)
    res.append(max)

    for i in range(k, n):
        max = arr[i]
        if (i == n - 1):
            res.append(arr[n - 1])

        else:
            for j in range(i + 1, n):
                if (max >= arr[j]):
                    continue
                else:
                    max = arr[j]
            if max not in res:
                res.append(max)

    return res


if __name__ == '__main__':
    #n=int(input())
    start=time.time()
    n=5
    #arr = list(map(int , input().split()))
    arr = [5,3,2,5,1]
    print("input : ",arr)
    ans =  getStarAndSuperStar(arr, n)
    print("stars output : ",ans)
    print("superstar : " , ans[0])
    end=time.time()
    print("time req :",end-start)


"""
    for i in range(k,n):
        print("i :",i)
        if(i==n-1):
            res.append(arr[i])
        else:
            for j in range(i+1,n):
                print("j :",j)
                if(arr[i]>arr[j]):
                    if(j==n-1):
                        res.append(arr[i])
                    else:
                        j+=1
                        continue
                        
                        
"""
