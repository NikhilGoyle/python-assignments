# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   7b-3
# Date:         10/12/2020
#
# list manipulation

#part a - median
list = [79,99,73,49,67,62,52,99,57,58,67,88,71,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,99,69,66,40,48,41,99,68,52,78,77,71,40,65,77,87,96,44,54,60,89,72]
#any list works
def medianFind(list):
    list = sorted(list)
    if len(list) % 2 == 1: #checks if odd
        median = list[(len(list))//2]    
    else: #if even
        median = (list[(len(list))//2-1]+list[len(list)//2])/2
    print("median:",median)
medianFind(list)
##########################################
#part b - fake sort
list = [79,99,73,49,67,62,52,99,57,58,67,88,71,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,99,69,66,40,48,41,99,68,52,78,77,71,40,65,77,87,96,44,54,60,89,72]
#using sample list
newlist = []

while len(list) > 0: #loops until all of the original list has been deleted
    min = list[0]
    minIndex = 0
    for num in range(len(list)): #loops through the entire list to find smallest number
        if list[num] < min: #finding minimum value in list
            min = list[num]      
            minIndex = num
    newlist.append(min) #adding the minimum value to the new array
    del list[minIndex] #removing the minimum value from the old array
print("sorted list:",newlist)

#reversing
revList = []
for num in range(len(newlist)):
    revList.append(newlist[-num-1]) #uses negative numbers on array to iterate through from back to front
print("reversed (sorted) list:",revList)

medianFind(newlist) #using fake sort to find the median (proving it works)