cities = int(input("Cities : "))
Arr = []
print("Array : ")
for i in range(cities):
    peoples = int(input())
    Arr.append(peoples)
buses = int(input("Buses : "))
cap = int(input("Capacity : "))

totalcap = buses*cap

for i in range(cities):
    totalcap = totalcap - Arr[i]

if (totalcap < 0):
    totalcap = 0-totalcap
else:
    totalcap = 0
print("Remains : ",totalcap)

