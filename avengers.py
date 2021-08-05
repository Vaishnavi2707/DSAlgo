# SHIELD Coding problem

class Avengers:
    def __init__(self,name,abilities,missionAssigned,missionCompleated):
        self.name=name
        self.abilities=abilities
        self.missionAssigned=missionAssigned
        self.missionCompleated=missionCompleated

    def display(self):
        print("Person name: ",self.name)
        print("Abilities: ",self.name)
        print("Mission Assigned: ",self.name)
        print("Mission Compleated: ",self.name)

def avengersPresent():
    Avenger1=Avengers("Captain America","")
    Avenger2=Avengers("Iron Man")
    Avenger3=Avengers("Hulk")
    Avenger4=Avengers("Thor")
    Avenger5=Avengers("Hawkeye")
    Avenger6=Avengers("Black Widow")


def one():
    if(allMissions):
        print(allMissions)
    else:
        print("No mission has been assigned to an Avenger.")

def two():
    print("Its 2")

#driver code
print("=======------S.H.I.E.L.D ------=========")
print("\nWelcome Captain Fury")
print("\n1. Check the missions \n"
      "2. Assign mission to Avengers \n"
      "3. Check mission's details\n"
      "4. Check Avenger's details\n"
      "5. Update Mission's status\n"
      "6. List Avengers\n"
      "7. Assign avenger to mission\n")

avengersPresent()

print("Enter the option: ")
choice=int(input())


allMissions = ['time machine']


if(choice==1):
    one()
elif(choice==2):
    two()
else:
    print("Enter valid input.")
















"""x= "hiuhdsiuh"
y=10
z="hgdjs"
e="uyet"
print("{:<30}|{:^5}|{:^20}|{:^10}".format(x,y,z,e))
"""