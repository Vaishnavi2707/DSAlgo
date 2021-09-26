
def checkPalindrome(s):
    os=s
    s = s.lower()
    l = 0
    h = len(s) - 1
    flag = 0
    while(l<h):
        if(s[l]==s[h]):
            flag = 1
            l+=1
            h-=1
            continue
        else:
            flag = 0
            break
    if(flag==1):
        res.append("%s is palindrome" %(os))
    else:
        res.append("%s is not palindrome" %(os))
    
        
def printOp(res):
    for i in res:
        print(i)
        
if __name__ =="__main__":
    res = []
    n = int(input())
    for i in range(n):
        s = input()
        checkPalindrome(s)
    printOp(res)
    
    
        
