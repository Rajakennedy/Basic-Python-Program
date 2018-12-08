import math
flag = 1
while flag:
    flag = 0
    try:
        radius = float(input("Enter the value:"))
        if radius == 0:
          print("Number should not be Zero")
          flag = 1
    except ValueError:
        print("Enter a Valid number")
        flag = 1

def Area(radius):
    return math.pi * radius * radius

print("Area of circle is", Area(radius))

flag = 1
while flag:
    flag = 0
    try:
        radius = float(input("Enter the value:"))
        if radius <= 0:
          print("Number should be Greater than Zero")
          flag = 1
    except ValueError:
        print("Enter a Valid number")
        flag = 1

def circumference(radius):

    return math.pi * radius * 2

print("Circumference of circle is", circumference(radius))
