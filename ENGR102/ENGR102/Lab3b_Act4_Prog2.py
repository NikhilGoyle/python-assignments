# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   4-2
# Date:         9/14/20
#
from math import *

print("This program calculates the angle between an observer and two other points")

main = []
p1 = []
p2 = []
#creates arrays to hold the coordinates
def function(array, name):
    print("Please enter the coordinates of the",name + ":")
    for x in range(3):
        coor = ""
        if x == 0:
            coor = "x: "
        if x == 1:
            coor = "y: "
        if x == 2:
            coor = "z: "
        array.append(float(input(coor)))
        print()
#function for accepting coordinates as input
function(main,"observer")
function(p1,"point 1")
function(p2,"point 2")
#accepts all 3 sets

v1 = []
v2 = []

for x in range(3):
    v1.append(p1[x]-main[x])
    v2.append(p2[x]-main[x])

#finds the vectors from the observer to the two points
v1mag = sqrt(v1[0]**2+v1[1]**2+v1[2]**2)
v2mag = sqrt(v2[0]**2+v2[1]**2+v2[2]**2)

#finds the magnitude of those 2 vectors
uv1 = []
uv2 = []

for x in range(3):
    uv1.append(v1[x]/v1mag)
    uv2.append(v2[x]/v2mag)
#finds the unit vector from the two vectors
uv1mag = sqrt(uv1[0]**2+uv1[1]**2+uv1[2]**2)
uv2mag = sqrt(uv2[0]**2+uv2[1]**2+uv2[2]**2)
#finds the magnitude of the unit vectors
dotprod = uv1[0]*uv2[0]+uv1[1]*uv2[1]+uv1[2]*uv2[2] #finds dot product

costheta = dotprod / (uv1mag*uv2mag) #simplifies the equation

angle = acos(costheta) #finds the angle in radians
finalAngle = angle*360/2/pi #converts angle to degrees

print("The angle between the observer and the two points is " + str(round(finalAngle,2)) + " degrees") 