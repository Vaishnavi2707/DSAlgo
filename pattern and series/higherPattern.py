"""
Program to print following pattern

Enter size : 6
1
3*2
4*5*6
10*9*8*7
11*12*13*14*15
21*20*19*18*17*16
"""



if __name__=="__main__":
    n = int(input("Enter size : "))
    count = 1
    for i in range(n):
        if(i&1 == 0):
            for j in range(0,i+1):
                print(count , end = "")
                count += 1
                if(i != j):
                    print("*" , end = "")
        else:
            x = count + i
            for j in range(0,i+1):
                print(x , end = "")
                x -= 1
                count += 1
                if(i != j):
                    print("*",end = "")
        print()
                

















        
        

"""
def rotate(s):
    l = 0
    h = len(s)-1
    while(l<h):
        temp = s[l]
        s[l] = s[h]
        s[h] = temp
        l+=1
        h-=1
    return s

if __name__ == "__main__":
    n = int(input("Size : "))
    x=1
    for i in range(n):
        s = []
        for j in range(0,i+1):
            s.append(x)
            s.append("*")
            x+=1
        if(i&1==1):
            rotate(s)
            for k in range(1,len(s)):
                print(s[k],end = "")
        else:
            for k in range(0,len(s)-1):
                print(s[k],end = "")
        print()

"""
