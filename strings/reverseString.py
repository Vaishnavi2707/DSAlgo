

"""using reversal algo"""
def reverse(s):
    l = 0
    h = len(s)-1
    while(l<h):
        temp = s[l]
        s[l] = s[h]
        s[h] = temp
        l+=1
        h-=1
    return s

s =input("Input String : ")
s = list(s)

s = reverse(s)
print("Reversed String : ",end = "")
for i in s:
    print(i,end = "")
    

"""Using Recursiondef reverse(s):
    if len(s) == 0:
        return s
    else:
        #print(s[1 :],s[0] )
        return reverse(s[1:]) + s[0]
s = input("Enter String :")
print("Input String :",s)
print("Reversed String : ",reverse(s))

"""

"""Reverse string using loop

def reverse(s):
    str = ""
    for i in s:
        str = i+str
    return str.lstrip()

s = input("Input string : ")
print("Reversed string :" , reverse(s))

"""
