# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   9b-1
# Date:         10/26/20
#

#this program reads a file called Celsius.txt and converts the temperature values to fahrenheit, then creates a file called Fahrenheit.txt to store them
celsiusFile = open("Celsius.txt")
fArray = [] #array to store values
for line in celsiusFile:
    fArray.append((float(line)*9/5) + 32) #iterates through the values in celsius and converts them to fahrenheit
celsiusFile.close()
fahrenheitFile = open("Fahrenheit.txt", 'w')
for i in fArray:
    fahrenheitFile.write(str(i)+"\n") #writes the stored fahrenheit values to the new file
    
