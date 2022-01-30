# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   4b-3
# Date:         9/21/20
# widget machine

print("This program will return the total number of widgets produced given the number of days the machine has been running.")
print("Note that the machine no longer produces widgets on day 100 or any day further.   ")
days = int(input("Please enter the number days (0-100): "))
if not(days >= 0) or not(days <=100):
    print("That number is not within the specified range.")
    raise SystemExit(0)

if days <= 10:
    widgets = 10*days
elif days <= 60:
    widgets = 40*(days-10)+100
else:
    widgets = 2100
    for day in range(0,days-60):
        widgets += 40 - (day+1) 
        
print(widgets,"widgets were produced in",days,"days.")
