# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   4b-4
# Date:         9/21/20
# quadratic
import math
import cmath

print("This program finds the roots of a quadratic given the coefficients A, B, and C in the model Ax^2+Bx+C = 0")
a = int(input("Please enter the value for A: "))
b = int(input("Please enter the value for B: "))
c = int(input("Please enter the value for C: "))
equation = str(a)+"x^2 + ("+str(b)+"x) + ("+str(c)+") = 0"
print()
if a != 0:
    if (b**2) - (4*a*c) < 0:
        root1 = str((-b + cmath.sqrt((b**2) - (4*a*c))) / (2 * a))
        root2 = str((-b - cmath.sqrt((b**2) - (4*a*c))) / (2 * a))#imaginary number case
    else:
        root1 = str((-b + math.sqrt((b**2) - (4*a*c))) / (2 * a))
        root2 = str((-b - math.sqrt((b**2) - (4*a*c))) / (2 * a))#non imaginary number case
    print("The roots of the quadtratic equation",equation,"are",root1.replace("j","i"),"and",root2.replace("j","i"))
elif a == 0 and b != 0:
    root = (-c / b)
    print("The root of the line",str(b)+"x + ("+str(c)+") = 0 is",root)
elif a == 0 and b == 0 and c != 0:
    print("This is not a valid equation. C must be '0' or either A or B must have a value.")
else:
    print("There is no line.")
    
