# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 4-1b
# Date:         9/14/2020
#


print("This program calculates kinetic energy given mass and velocity")

mass = float(input("Please enter the mass (g): "))
velocity = float(input("Please enter the velocity (m/s): "))
kineticEnergy = .5*mass*velocity**2 # joules
print()
print("The Kinetic energy of a given object is",round(kineticEnergy,4), "J") #kinetic energy in joules

