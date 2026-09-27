#PROGRAM TO BUILD A PROJECTILE MOTION CALCULATOR USING BASIC PYTHON FUNCTIONS AND LIBRARIES
import math as m
def t_flight(v,angle):
    x=m.radians(angle)
    time = (2*v*m.sin(x))/10
    return time
def max_height(v,angle):
    x=m.radians(angle)
    height = ((v**2)*(m.sin(x)**2))/20
    return height
def t_range(v,angle):
    m=m.radians(angle)
    range = ((v**2)*(sin(2*x)))/ 10
    return range
ans = 'y'
while ans == 'y':
    print("WELCOME")
    print("please make a choice from the below listed options")
    print("1. Time of flight")
    print("2. Maximum Height")
    print("3. Range of projectile motion")
    s = int(input(" Enter the corresponding number of your preferred option:"))
    vel = int(input("Enter the velocity of the object:"))
    ang = float(input("Enter the angle of projection:"))
    if s==1:
        t=t_flight(vel,ang)
        print("The time of flight will be :",t)
    elif s==2:
        h=max_height(vel,ang)
        print("The maximum height will be :",h)
    elif s==3:
        a = t_range(vel,ang)
        print("The range will be :",a)
    else:
        print("invalid input")
    ans = input("Do you want to continue?(y/n)")
print("THANK YOU!!!")
    
    
            
