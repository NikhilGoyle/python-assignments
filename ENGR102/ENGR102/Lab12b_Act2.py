# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   12b-2
# Date:         17/11/2020
#
def evalCubic(clist, xval):
    return clist[0]*xval**3+clist[1]*xval**2+clist[2]*xval+clist[3]

print("This program will find a root for a cubic polynomial")
inputStr = input("Please enter the 4 coefficients of the polynomial in order, separated by spaces: ")
coefficients = inputStr.split()
if len(coefficients) != 4:
    print("Please enter exactly 4 values")
    raise SystemExit
for num in range(len(coefficients)):
    try: coefficients[num] = int(coefficients[num])
    except: 
        print("Please enter integer values. Try again.")
        raise SystemExit
#same input as previous program       
        
boundA = int(input("Please enter the lower bound of the interval containing a root: "))
boundB = int(input("Please enter the upper bound of the interval containing a root: "))
tol = 1e-6
count = 0
while boundB-boundA > tol: #repeats until the width of the bisection is respectably small
    count += 1
    P = (boundB+boundA)/2
    if evalCubic(coefficients,P) < 0:
        boundA = P
    if evalCubic(coefficients,P) > 0:
        boundB = P
    elif evalCubic(coefficients,P) == 0: #case for if the root is exactly on the bisection
        boundB = P
        boundA = P
        break
print("The root lies in the interval {:.7f} to {:.7f} within a tolerance of {}".format(boundA,boundB,tol))
print("Iterations required:",count)

# =============================================================================
# TEST CASES
# format:
# input for polynomial
# lower bound
# upper bound
# explanation
# 
# -5 14 2 -10
# -10
# 1
# root is very close to 1 but just underneath
# 
# 2 2 2 2
# -2
# 0
# root is at -1 exactly, so the code should handle landing exactly on the bisection
# 
# -16 -20 500 45
# -5
# 5
# multiple roots, ~ -6,0,5 however bounds include only 1
# 
# 5 -10 15 -20
# -100
# 100
# testing large bounds ,root at ~1.5
# =============================================================================
