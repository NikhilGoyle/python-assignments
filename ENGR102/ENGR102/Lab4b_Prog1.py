# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   4b-1
# Date:         9/21/20
#

print("This program determines the largest number. Please enter 3 numbers: ")
one = int(input("Number 1: "))
two = int(input("Number 2: "))
three = int(input("Number 3: "))

max = one
if two > max:
    max = two
if three > max:
    max = three
print(max,"is the largest number")



