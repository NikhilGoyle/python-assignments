# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 2b-3
# Date:         9/7/2020
#

x = 1
y = 10
z = 0

z += x
print(z)

x += 1
z += x
print(z)

x = 1
y += x
z = 0
z += y
print(z)

z += y
x += 1
x += 1
x += 1
x += 1
x += 1
z += x
print(z)

x = y
y *= x
x = 1
y += x
y += x
z = 0
z += y
print(z)

y = 10
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
z = 0
z += y
print(z)

