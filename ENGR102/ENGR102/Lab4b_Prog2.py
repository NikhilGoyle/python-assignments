# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   4b-2
# Date:         9/21/20
#

print("This program calculates the Reynolds number given velocity, pipe diameter, and viscosity. Please enter the specified values.")
velocity = int(input("velocity: "))
diameter = int(input("diameter: "))
viscosity = int(input("viscosity: "))
reynolds = velocity*diameter/viscosity
print()
if reynolds < 2300:
    print("The Reynolds number is",reynolds,"and is laminar")
elif reynolds > 2900:
    print("The Reynolds number is",reynolds,"and is fully turbulent")
else:
    print("The Reynolds number is",reynolds,"and is in transition")





