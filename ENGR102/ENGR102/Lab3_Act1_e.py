# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
#               Aiden Devlin
#               Amanda Macha
#               Travis Byrd
# Section:      ENGR102 - 216
# Assignment:   Lab 3-1 e
# Date:         9/11/20
#

print("This program converts miles per hour to meters per second")
mph = int(input("Please enter the number of miles per hour to be converted to meters per second: ")) #saves input as mph
mps = 0.44704*mph #converts mph to mps
print(mph,"mile(s) per hour is equivalent to",round(mps,4),"meter(s) per second")
