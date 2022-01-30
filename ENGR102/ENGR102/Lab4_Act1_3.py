# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   lab 4-1
# Date:         9/21/20
#
#This program compares values using tolerances
a = 1/7
print(a)
b = a*7
print(b)

print()

TOL = 1e-10
a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print("b and e are equal within tolerance of", TOL)
else:
    print("b and e are NOT equal within tolerance of", TOL)

print()

from math import *
TOL = 1e-10
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
if abs(y-z) < TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of", TOL)