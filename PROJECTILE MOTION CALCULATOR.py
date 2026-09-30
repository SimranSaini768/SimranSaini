# PROGRAM TO BUILD A PROJECTILE MOTION CALCULATOR USING BASIC PYTHON FUNCTIONS AND LIBRARIES
import math as m

def t_flight(v, angle):
    a = m.radians(angle)
    time = (2 * v * m.sin(a)) / 10
    return time

def max_height(v, angle):
    a = m.radians(angle)
    height = ((v ** 2) * (m.sin(a) ** 2)) / 20
    return height

def t_range(v, angle):
    a = m.radians(angle)
    rng = ((v ** 2) * (m.sin(2 * a))) / 10
    return rng

ans = 'y'
while ans == 'y':
    print("WELCOME")
    print("Please make a choice from the below listed options")
    print("1. Time of flight")
    print("2. Maximum height")
    print("3. Range of projectile motion")
    x = int(input(" Enter the corresponding number of your preferred option:"))
    if x == 1:
        vel = int(input("Enter the velocity of the object:"))
        ang = float(input("Enter the angle of projection:"))
        t = t_flight(vel, ang)
        print("The time of flight will be :", t)
    elif x == 2:
        vel = int(input("Enter the velocity of the object:"))
        ang = float(input("Enter the angle of projection:"))
        h = max_height(vel, ang)
        print("The maximum height will be :", h)
    elif x == 3:
        vel = int(input("Enter the velocity of the object:"))
        ang = float(input("Enter the angle of projection:"))
        r = t_range(vel, ang)
        print("The range will be :", r)
    else:
        print("Invalid input")
    ans = input("Do you want to continue?(y/n)")
print("THANK YOU!!!")
