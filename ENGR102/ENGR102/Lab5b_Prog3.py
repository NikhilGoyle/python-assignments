# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   5b-3
# Date:         9/28/20
#

print("This program will complete a MacLaurin series estimation to a degree of 1e-6")
x = float(input("Please enter a value between -1 and 1: "))
if float(x) < -1 or float(x) > 1:
    raise SystemExit
    
sum = 1
tol = 1*10**-6
count = 0
true = 1/(1-x)
while abs(sum-true) > tol:
    count +=1
    sum += x**count
    
print("X: {:0.4}".format(x))
print("Estimated summation:",sum)
print("Number of terms used:",count)
print("Exact value: {:0.6f}".format(true))
print("Difference between estimation and exact: {:0.8f}".format(sum-true))



