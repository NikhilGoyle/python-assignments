# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 2b-1
# Date:         9/7/2020
#

print("My name is Nikhil Goyle. My UIN is 3300011177. I am enrolled in section 216")
print("I have been playing the guitar since I was 10")

resistance = 20 # ohms
current = 5 #amperes
voltage = resistance * current #ohms * amperes -> volts
print("The voltage of a given conductor is", voltage ,"V") #voltage of a conductor in volts


mass = 100 #kilograms
velocity = 21 #meters/second
kineticEnergy = .5*mass*velocity**2 # joules
print("The Kinetic energy of a given object is",kineticEnergy, "J") #kinetic energy in joules


fluidVelocity = 100 #meters/second
viscosity = 1.2 #meters^2/second
linearDim = 2.5 #meters
reynoldsNum = fluidVelocity*linearDim/viscosity #units cancel out (no units)
print("The Reynolds Number of a given fluid is", reynoldsNum,) #is a coefficient/no units

