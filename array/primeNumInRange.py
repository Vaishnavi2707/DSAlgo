
def checkPrime(p):
    root = p//2
    for i in range(2,root+1):
        if(p%i == 0):
            return False
        
    return True

if __name__ == "__main__":
    start = int(input("Enter starting point : "))
    end = int(input("Enter ending point : "))

    for i in range(start,end+1):
        if(i>1):
            if(checkPrime(i)):
                print(i,end = " ")
                

"""

#prime nums in range
if __name__ == "__main__":
    s= int(input("Enter starting point: "))
    e= int(input("Enter ending point: "))
    primeNums=[]
    for i in range(s,e+1):
        if i>1:
            halt=int(i//2)
            for j in range(2,halt):
                if(i%j == 0):
                    break
            else:
                primeNums.append(i)

    print("prime numbers between " ,s ," and " ,e ,"are :")
    print(primeNums , end=", ")




"""

"""

#check prime numbers divisibility

def nextstep(m):
    for k in primes1:
        if(m%k == 0):
            print(m," is divisible by primes above 100 , i.e. : ",k)
            pass

primes = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes1=[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
notdiv = []
for i in range(1000,2000):
    for j in primes:
        if(i%j == 0):
            break
        else:
            if i not in notdiv:
                notdiv.append(i)

print("Not divisible by primes till 100 : ",notdiv)

for m in notdiv:
    nextstep(m)

"""















"""
def checkPrime(num):
    count = 1    #for 1
    half = int(num/2) +1
    for j in range(2,half,1):
        if(num % j == 0):
            count = count+1
            break
    return num

def printPrime(s,e,primeNums):
    si = primeNums.index(s,0)
    ei = primeNums.index(e,0)
    print("prime numbers between " ,s ," and " ,e ,"are :")
    print(primeNums[si:ei],end=" ")

if __name__ == "__main__":
    s= int(input("Enter starting point: "))
    e= int(input("Enter ending point: "))

    primeNums = []

    for i in range(2,e+1):
        if(checkPrime(i)==i):
            primeNums.append(i)

    print(primeNums)
    printPrime(s,e,primeNums)

"""
