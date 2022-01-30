# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   5b-1
# Date:         9/28/20
#

print("This program takes in a positive integer and computes the Collatz sequence.")
num = int(input("Please enter a positive integer: "))
count = 0
array = [num]

while num != 1:
    if num % 2 == 0:
        num = num/2
        count +=1
        array.append(int(num))
    else:
        num = (3*num)+1
        count +=1 
        array.append(int(num))
print("Sequence:",array)
print("Number of iterations:",count)