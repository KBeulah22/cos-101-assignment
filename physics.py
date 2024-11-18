print("WELCOME TO COS 101")
print("Name: Beulah  ")
print("Matric number: " )
def a():
    velocity = float(input("enter value for velocity: "))
    time = float(input("enter value for time: "))
#   acceleration= velocity * time
    acceleration =str(velocity * time)
    print("Acceleration= :" +acceleration+"m/s^2")

def b():
    distance = float(input("enter value for distance: "))
    time = float(input("enter value for time: "))
 #   speed= distance / time
    speed= str(distance / time)
    print("Distance= :" +speed+"m/s")

def c():
    force = float(input("enter value for force: "))
    distance = float(input("enter value for distance: "))
 #  work= force * distance
    work = str(force * distance)
    print(work)

def d():
    charge = int(input("enter value for charge: "))
    distance = int(input("enter value for distance: "))
    shocker=str(charge * distance)
    print(shocker)

def e():
    displacement = float(input("enter value for displacement: "))
    velocity = float(input("enter value for velocity: "))
    time = str(displacement / velocity)
    print(time)

def main():
    User_choice = input("Welcome to cos 101! Enter your choice: ")

    if User_choice == "a":
        a()
    elif User_choice == "b":
        b()
    elif User_choice == "c":
        c()
    elif User_choice == "d":
        d()
    elif User_choice == "e":
        e()
if __name__ == "__main__":
     main()