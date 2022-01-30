# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   5b-2
# Date:         9/28/20
#

print("This program will accept positive data values and calculate the average, maximum, and minimum of those values. A negative number indicates the end of the data set.")
imp = float(input("Please enter a data element, or a negative number to indicate there are no more data elements: "))
if imp> 0:
    max = imp
    min = imp
    cumulative = imp
    count = 1
else:
    print("That is not an acceptable value. Please try again with a positive value.")
    raise SystemExit
       
while True:
    inp = float(input("Please enter a data element, or a negative number to indicate there are no more data elements: "))
    if inp < 0:
        break
    if inp > max:
        max = inp
    if inp < min:
        min = inp
    cumulative += inp
    count += 1
    
print()
print("Average:",float(cumulative)/count)
print("Maximum:",max)
print("Minimum:",min)

