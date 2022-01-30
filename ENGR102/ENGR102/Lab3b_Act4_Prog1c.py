# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 4-1c
# Date:         9/14/2020
#


print("This program calculates the Reynolds number given fluid velocity, viscosity, and the linear dimension")
fluidVelocity = float(input("Please enter the velocity of the fluid: "))
viscosity = float(input("Please enter the viscosity of the fluid: "))
linearDim = float(input("Please enter the linear dimension of the fluid: "))
reynoldsNum = fluidVelocity*linearDim/viscosity #units cancel out (no units)
print()
print("The Reynolds Number of a given fluid is", round(reynoldsNum,4),) #is a coefficient/no units

