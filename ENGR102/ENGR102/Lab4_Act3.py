# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
#               Travis Byrd
#              	Aiden Devlin
#              	Amanda Macha
# Section:      ENGR102 - 216
# Assignment:   4b-3
# Date:         9/21/20
#

inp = input("Please enter 'True' or 'False' for value a: ")
if inp == "True" or inp == "T" or inp == "t":
    a = True
elif inp == "False" or inp == "F" or inp == "f":
    a = False
else:
    print("Please enter an accepted value")
    
inp = input("Please enter 'True' or 'False' for value b: ")
if inp == "True" or inp == "T" or inp == "t":
    b = True
elif inp == "False" or inp == "F" or inp == "f":
    b = False
else:
    print("Please enter an accepted value")
    
inp = input("Please enter 'True' or 'False' for value c: ")
if inp == "True" or inp == "T" or inp == "t":
    c = True
elif inp == "False" or inp == "F" or inp == "f":
    c = False
else:
    print("Please enter an accepted value")
#end of part a
print()
print("a and b and c:",a and b and c)
print("a or b or c:",a or b or c)
#end of part b
a = True
b = True
c = False
print()
print("Using the hard coded values for a,b,c respectively",a,b,c)
print("a xor b:",(not(a and b) and (a or b)))
print("odd number of 'True':",(not((not(a and b) and (a or b)) and c) and ((not(a and b) and (a or b)) or c)))    
     
################################################
# =============================================================================
# a2 = True
# b2 = False
# c2 = False
# print(not(a2 and b2) and (a2 or b2)) #xor
# axorb = (not(a2 and b2) and (a2 or b2))
# print(not((not(a2 and b2) and (a2 or b2)) and c2) and ((not(a2 and b2) and (a2 or b2)) or c2)) #odd number of trues
# 
# =============================================================================

