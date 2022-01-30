# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   7b-2
# Date:         10/12/2020
#
#vectors
from math import *
print("This program takes in two vectors with as many dimensions as desired and returns some information about them.")
try: dimensions = int(input("Please enter the number of dimensions of the vectors: "))
except: 
    print("Please enter values in the correct format")
    raise SystemExit
vectorA = []
vectorB = []
for num in range(dimensions):
    try: vectorA.append(float(input("Please enter the value for dimension " + str(num+1) + " for the first vector: ")))
    except: 
        print("Please enter values in the correct format")
        raise SystemExit
for num in range(dimensions):
    try: vectorB.append(float(input("Please enter the value for dimension " + str(num+1) + " for the second vector: ")))
    except: 
        print("Please enter values in the correct format")
        raise SystemExit
sum = 0
for val in vectorA:
    sum += float(val)**2
magnitudeA = sqrt(sum)
sum = 0
for val in vectorB:
    sum += float(val)**2
magnitudeB = sqrt(sum)

sumVector = []
for val in range(dimensions):
    sumVector.append(vectorA[val]+vectorB[val])
    
diffVector = []
for val in range(dimensions):
    diffVector.append(vectorA[val]-vectorB[val])
    
dpsum = 0
for val in range(dimensions):
    dpsum += float(vectorA[val]*vectorB[val])

print("Vector A:",vectorA)
print("Vector B:",vectorB)
print("Magnitude of Vector A:",magnitudeA)
print("Magnitude of Vector B:",magnitudeB)
print("Vector A + Vector B:",sumVector)
print("Vector A - Vector B:",diffVector)
print("The Dot Product of Vectors A and B:",dpsum)