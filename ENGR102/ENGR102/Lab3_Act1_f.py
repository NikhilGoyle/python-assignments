# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
#               Aiden Devlin
#               Amanda Macha
#               Travis Byrd
# Section:      ENGR102 - 216
# Assignment:   Lab 3-1 f
# Date:         9/11/20
#

print("This program converts Fahrenheit to Celsius")
F = int(input("Please enter the number of degrees Farehnheit to be converted to degrees Celsius: ")) #saves input as deg. F
C = (5/9)*(F-32) #converts deg. F to deg. C
print(F,"degrees Fahrenheit is equivalent to",round(C,4),"degrees Celsius")