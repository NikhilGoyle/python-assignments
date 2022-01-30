# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   11b
# Date:         11/9/2020
#
import math as m

def materialRemaining(length, width, height, radius):
    if radius > min(length/2, width/2) or radius < 0: #checks radius size
        return "The radius is not valid"
    boxVol = length*width*height #volume of the box
    cylVol = m.pi*(radius**2)*height #volume of the drilled hole
    return boxVol-cylVol

def profitability(names, costs, value):
    min = float(value[0])-float(costs[0])
    minIndex = 0
    for num in range(len(names)):
        if float(value[num])-float(costs[num]) < min: #checks to see which has the worst profitability
            min = float(value[num])-float(costs[num])
            minIndex = num
    return names[minIndex] + " is the least profitable facility with a net of " + str(min)    

def information(name,city,state,zip,address1,address2 = ""):
    print(name)
    print(address1)
    if len(address2) > 0:#only uses address2 extra line if there is one
        print(address2)
    print(city + ",",state,zip)
    
def mmm(floats):
    total = 0
    min = floats[0]
    max = floats[0]
    for num in floats:
        total += num
        if num < min:
            min = num
        if num > max:
            max = num
    string = [max]
    string.append(min)
    string.append(total/len(list)) 
    return string # returns max, min, and avg respectively

def velocities(times,positions):
    speeds = []
    previousTime = times[0]
    previousPos = positions[0]
    for i in range(1,len(times)):
        speeds.append((positions[i]-previousPos)/(times[i]-previousTime)) #calculation for velocity
        previousTime = times[i]
        previousPos = positions[i]
    return speeds

###########################################TEST CASES####################################################
#1
print(materialRemaining(1,1,1,.5))

#2  
facilityName = [ 'ABC Corporation', 'General Manufacturing', 'Specialty Products'   ]
annualCost = [75.1, 103.8, 99.2]
annualValue = [135.7, 200.1, 188.3]
print(profitability(facilityName,annualCost,annualValue))
            
#3
name = "Nick Franklin"
city = "College Station"
state = "TX"
zip = "77845"
address1 = "123 Apple St."
address2 = "Apartment 3, Room 4"
information(name,city,state,zip,address1)#works with or without address2

#4
list = [234,345,467,45,324,43,54,6,57,45,35.456,3244,554,6435.465,-5,0]
print(mmm(list)) 

#5
times = [1,2,4,6,7,9,12,35]
positions = [0,12,15,47,345,5468,34,3]
print(velocities(times,positions)) #mostly positive and increasing velocities, some neg at the end

 










