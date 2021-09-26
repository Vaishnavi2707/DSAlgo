

def interest(p):
    rate = 10.75 / 12
    iGenerated = (p*rate)/100
    return iGenerated

principal = 1000000
emi = 21618
months = 60
totalEMI = emi*months
oneYearEmi = emi*12
for i in range(1,61):
    inter = interest(principal)
    balance = principal - emi
    balance = balance + inter
    print("Month %d  : %d - %d = %d + %d" %(i,principal,emi,balance , inter))
    principal = balance
    
