
def checkPalindrome(s):
    l = 0
    h = len(s) - 1
    while(l<h):
        if(s[l]==s[h]):
            flag = 1
            l+=1
            h-=1
            continue
        else:
            return False
    return True
        
def main():
    s = input("Enter string : ")
    if(checkPalindrome(s)):
        print(s ,"is a palindrome.")
    else:
        print(s ,"is not a palindrome.")
    main()

if __name__=="__main__":
    main()


