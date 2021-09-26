# Program to check if a number is prime or not  most efficient solution

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    #range(2,math.floor(math.sqrt(num))) or square root
    for i in range(2, num//2):
        #print(i)
        if(num % i) == 0:
            print(num, "is not a prime number")
            print(i, "*", int(num / i), "=", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than or equal to 1, it is not prime
else:
    print(num, "is not a prime number")












"""
# Program to check if a number is prime or not
num = int(input("Enter a number: "))

flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

"""







"""
import time

def checkroot(n):
    end = int(n/3)+1
    for i in range(1,end):
        sq=i*i
        if(sq == n):
            return "Not Prime"
        elif(sq > n):
                return i

def getSeries(e):
    for i in range(2,e+1):
        if i>1:
            half=int(i/2)
            for j in range(2,half):
                if(i%j == 0):
                    break
            else:
                primeNums.append(i)

    print("Prime numbers till " ,e ,"are :",primeNums)

def checkPrime(n,primeNums):
    count=0
    for i in primeNums:
        if(n%i == 0):
            count=count+1
    if(count>0):
        return "Not Prime"
    else:
        return "Prime"


if __name__ == "__main__":
    start = time.time()
    n = int(input("Enter the number : "))
    lowest_num = checkroot(n)
    if(lowest_num == "Not Prime"):
        Result = "Not Prime"
    else:
        primeNums = []
        getSeries(lowest_num)
        Result = checkPrime(n, primeNums)

    print(Result)
    end = time.time()
    print("Total Time required : ",end," - ",start ," = ",end-start)

"""
"""
def checkprime():
    n = int(input("Enter the number : "))
    primes=[2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in primes:
        if(n==i):
            print("Prime")
            break
        if(n%i == 0):
            print("Not prime , divisor  = ",i)
            break
    else:
        print("Prime")

    if(n==1):
        return
    else:
        checkprime()
"""
