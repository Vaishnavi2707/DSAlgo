#DIvision without / and %
def div(num,den):
    i=1.0
    for i in range(num):
        temp=den*i
        if(temp == num):
            res=i
            break
    return res

def main():
    num , den = float(input("Enter Numerator : ")) , float(input("Enter Denominator : "))
    print(num,den,type(num),type(den))
    res = div(num , den)
    print("Result = ",res)
    print()
    main()

if __name__=='__main__':
    main()