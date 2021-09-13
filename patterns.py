#Patterns

n = 5
print("1")
for i in range(0,n,1):
    for j in range(i,n,1):
        print("*",end=" ")
    print()
    
print("2")
for i in range(0,n,1):
    for j in range(0,i+1,1):
        print("*",end=" ")
    print()

print("3")
for i in range(0,n,1):
    for j in range(i,n-1,1):
        print(" ",end=" ")
    for k in range(0,i+1,1):
        print("*",end=" ")
    print()



print("4")
for i in range(0,n,1):
    for j in range(i,n-1,1):
        print(" ",end=" ")
    for k in range(0,i+1,1):
        print("*",end=" ")
    for k in range(0,i,1):
        print("*",end=" ")
    print()
    
print("5")
for i in range(0,n,1):
    for k in range(0,i+1,1):
        print("*",end=" ")
    for k in range(0,i,1):
        print("#",end=" ")
    print()
     
print("6")
for i in range(0,n,1):
    for j in range(i,n-1,1):
        print("*",end=" ")
    for k in range(0,i+1,1):
        print("#",end=" ")
    print()

print("7")
for i in range(0,n,1):
    for j in range(i,n,1):
        print("*",end=" ")
    for k in range(0,i,1):
        print("2",end=" ")
    for k in range(0,i+1,1):
        print("3",end=" ")
    for l in range(i,n,1):
        print("*",end=" ")
    print()

print("8")
for i in range(0,n,1):
    for j in range(i,n,1):
        print("*",end=" ")
    for k in range(0,i,1):
        print(i+1,end=" ")
    for k in range(0,i+1,1):
        print(i+1,end=" ")
    for l in range(i,n,1):
        print("*",end=" ")
    print()

print("9")

for i in range(0,n,1):
    num =9
    for j in range(n,i,-1):
        print("*",end=" ")
    for k in range(i,0,-1):
        print(num,end=" ")
        num-=1
    for k in range(i+1,0,-1):
        print(num,end=" ")
        num-=1
    for l in range(n,i,-1):
        print("*",end=" ")
    print()
print("10")
for i in range(0,n,1):
    for j in range(i,n-1,1):
        print(" ",end=" ")
    for k in range(0,i+1,1):
        print("*",end=" ")
    for k in range(0,i,1):
        print("*",end=" ")
    print()
for i in range(0,n-1,1):
    for j in range(0,i+1,1):
        print(" ",end=" ")
    for k in range(i+1,n-1,1):
        print("*",end=" ")
    for k in range(i+1,n,1):
        print("*",end=" ")
    print()


"""
1
* * * * * 
* * * * 
* * * 
* * 
* 
2
* 
* * 
* * * 
* * * * 
* * * * * 
3
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
4
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
5
* 
* * # 
* * * # # 
* * * * # # # 
* * * * * # # # # 
6
* * * * # 
* * * # # 
* * # # # 
* # # # # 
# # # # # 
7
* * * * * 3 * * * * * 
* * * * 2 3 3 * * * * 
* * * 2 2 3 3 3 * * * 
* * 2 2 2 3 3 3 3 * * 
* 2 2 2 2 3 3 3 3 3 * 
8
* * * * * 1 * * * * * 
* * * * 2 2 2 * * * * 
* * * 3 3 3 3 3 * * * 
* * 4 4 4 4 4 4 4 * * 
* 5 5 5 5 5 5 5 5 5 * 
9
* * * * * 9 * * * * * 
* * * * 9 8 7 * * * * 
* * * 9 8 7 6 5 * * * 
* * 9 8 7 6 5 4 3 * * 
* 9 8 7 6 5 4 3 2 1 * 
10
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
>>> 
"""
