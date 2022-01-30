# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   10b-1
# Date:         11/3/2020
#
import numpy as np

X = np.array([1.0,3.5,5.2,7.3,9.5])
Y = np.array([2.0,4.3,10.0,15.0,22.0])

sumX = sum(X)
sumY = sum(Y)
sumX2 = sum(X**2)
sumXY = sum(X*Y)

a0 = ((sumY*sumX2)-(sumX*sumXY))/(5*sumX2-sumX*sumX)
a1 = (5*sumXY-sumY*sumX)/(5*sumX2-sumX*sumX)

print("a0 = {:.4f}".format(a0))
print("a1 = {:.4f}".format(a1))