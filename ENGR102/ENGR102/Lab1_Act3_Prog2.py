# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 1b-2
# Date:         8/29/2020
#
import math

print("This shows the evaluation of sin(x)/x as x approaches 0")
print("My guess is '1'")

x = 1
for num in range(8):
    print(math.sin(x)/x)
    x= x/10
    
print()

print("This shows the evaluation of 1-cos(x)/x^2 as x approaches 0")
print("My guess is 0")

x = 1
for num in range(8):
    print((1-math.cos(x))/x**2)
    x = x/10

print()

print("This shows the evaluation of (1+(1/x))^x as x approaches infinity")
print("My guess is 2")

x = 1
for num in range(8):
    print((1+(1/x))**x)
    x = x*10