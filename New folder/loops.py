# akhi java loops HackerRank


def series(a,b,n):
    res = []
    s = a + b
    res.append(s)
    for i  in range(1,n):
        t = 2**i
        s = s + (b*t)
        res.append(s)
    return res


lofl = []
q = int(input())
for i in range(q):
    a,b,n = map(int,input().split())
    lofl.append(series(a,b,n))

for i in range(q):
    l = lofl[i]
    for j in l:
        print(j,end = " ")
    print()
        
