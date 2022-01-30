# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 4-1a
# Date:         9/14/2020
#

print("This program calculates voltage given resistance and current")

resistance = float(input("Please enter the resistance (ohms): "))
current = float(input("Please enter the current (amperes): "))
voltage = resistance * current #ohms * amperes -> volts
print()
print("The voltage of a given conductor is", round(voltage,4) ,"V") #voltage of a conductor in volts

