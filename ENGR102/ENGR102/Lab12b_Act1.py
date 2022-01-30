# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   12b-1
# Date:         17/11/2020
#
import numpy
import matplotlib.pyplot as mpl

def evalCubic(clist, xval): #evaluates f(x)
    return clist[0]*xval**3+clist[1]*xval**2+clist[2]*xval+clist[3]

print("This program will plot a cubic polynomial")
inputStr = input("Please enter the 4 coefficients of the polynomial in order, separated by spaces: ")
coefficients = inputStr.split() #splits the one line of input into an array of coefficients
if len(coefficients) != 4:
    print("Please enter exactly 4 values")
    raise SystemExit
for num in range(len(coefficients)):
    try: coefficients[num] = int(coefficients[num])
    except: 
        print("Please enter integer values. Try again.")
        raise SystemExit 
#code takes in input only if it follows the format of 4 values and all are integers

x = input("Please enter an x value to evaluate the polynomial at: ")
try: x = int(x) #makes sure the input is integer
except: print("Please enter an integer value for x. Try again.") 
print("f(x) for the x value",x,"=",evalCubic(coefficients, x))

plotx = numpy.linspace(-10,10,21) #plot x range is -10 to 10 which tends to cover the roots
tempy = []
for num in plotx:
    tempy.append(evalCubic(coefficients,num))
    #ploty = numpy.append(ploty,evalCubic(coefficients,num))
ploty = numpy.array(tempy)

mpl.plot(plotx,ploty,"o",label = "hi")
mpl.xlabel("X Values")
mpl.ylabel("Y Values")
mpl.title("Plot of cubic polynomial")
mpl.legend()