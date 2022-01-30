# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   6b-2
# Date:         10/5/20
#

# =============================================================================
# O: (0,0)
# A: (0.01, 44) 
# C: (0.06, 44) 
# D: (0.18, 60) 
# E: (0.26, 50)
# points 
# =============================================================================
print("This program estimates stress for structural steel in tension when given strain")
slopeone = (44-0)/(0.01-0)
slopetwo = (44-44)/(0.06-0.01)
slopethree = (60-44)/(.18-.06)
slopefour = (50-60)/(.26-.18) #y1-y2/x1-x2 slope formula
initialone = 0
initialtwo = 44
initialthree = 44
initialfour = 60 # y values

strain = float(input("Please enter a value for strain between 0.00 and 0.26: "))
stress = float
if 0<=strain<=.26: #checks valid input
    if 0<=strain<.01: 
        stress = (slopeone*(strain-0))+initialone
    elif .01<=strain<.06:
        stress = (slopetwo*(strain-.01))+initialtwo
    elif .06<=strain<.18:
        stress = (slopethree*(strain-0.06))+initialthree
    elif .18<=strain<=.26:
        stress = (slopefour*(strain-.18))+initialfour #calculates y value for all 4 segements/regions
    print("The stress is approximately {0:.1f} ksi".format(stress)) #prints with 1 decimal place
else: #case for invalid input
    print("That value does not fit the model. Please try again.")
    raise SystemExit    
    
    