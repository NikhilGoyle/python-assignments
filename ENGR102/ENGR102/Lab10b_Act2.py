# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   10b-2
# Date:         11/2/2020
#
import numpy as np

W = 900.0

A = np.array([[-np.cos(40/360*2*np.pi),np.cos(55/360*2*np.pi)],[np.sin(40/360*2*np.pi),np.sin(55/360*2*np.pi)]])
b = np.array([[0],[W]])

result = np.linalg.solve(A,b)
print("At a weight of W =",W)
print("The tension in the tethers are T1 = {:.1f} lbf and T2 = {:.1f} lbf".format(result[0][0],result[1][0]))
print()
maxT = result[1][0]
while (maxT) < 800:
    W += 5
    A = np.array([[-np.cos(40/360*2*np.pi),np.cos(55/360*2*np.pi)],[np.sin(40/360*2*np.pi),np.sin(55/360*2*np.pi)]])
    b = np.array([[0],[W]])
    result = np.linalg.solve(A,b)
    if result[0][0] > 800 or result[1][0] > 800:
        W -= 5
        break
    T1 = result[0][0]
    T2 = result[1][0]
    if T1 > maxT:
        maxT = T1
    if T2 > maxT:
        maxT = T1
print("The largest weight that can be safely supported is {:.0f} lbs at T1 = {:.1f} lbf and T2 = {:.1f} lbf".format(W,T1,T2))