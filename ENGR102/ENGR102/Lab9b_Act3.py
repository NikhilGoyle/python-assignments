# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   9b-3
# Date:         10/26/20
#

loan = open("LoanExample.csv") #what i chose to name the file created in lab 9b-2
for line in loan:
    lineArray = line.split(",")
    column = 1
    print()
    for num in lineArray:
        if column == 1:
            try:formatted = (int(num)) #4 decimals for the first column (T)
            except:formatted = num
        elif column == 2:
            try:formatted = "{:.2f}".format(float(num)) #2 decimals for money
            except:formatted = num
        elif column == 3 or column == 4:
            try:formatted = "{:.2f}".format(float(num)) 
            except:formatted = num
        else:
            formatted = num
           
        column += 1
        print("{:>18}".format(formatted), end="") #format and print the last column (s)