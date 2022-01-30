# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   Lab 2b-2c
# Date:         9/7/2020
#

# t=13, (1,3,7)
# t=84, (23,-5,10)
# find position at t=50
for num in range(0, 5):
    initial = 13 
    final = 84
    input = 20+num*7.5
    #t coordinates (given)
    
    tdiff = final-initial
    xslope = (23-1)/tdiff
    yslope = (-5-3)/tdiff
    zslope = (10-7)/tdiff
    #finds the amount by which 1 increase in t will affect x y and z
    
    tinc = input-initial #how far the desired point is from a reference point
    
    xval = tinc*xslope+1
    yval = tinc*yslope+3
    zval = tinc*zslope+7
    #finds the increase from the initial point and adds it to the initial point to get the final coordinates
    print("time of interest =",input,"seconds")
    print("x0 =",xval,"m")
    print("y0 =",yval,"m")
    print("z0 =",zval,"m")
    print("---------------------")