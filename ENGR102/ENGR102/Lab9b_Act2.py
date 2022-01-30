# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Nikhil Goyle
# Section:      ENGR102 - 216
# Assignment:   9b-2
# Date:         10/26/20
#

print("This program takes information about a loan and does some calculations.")
filename = input("Please enter an appropriate file name to save the loan data (without file extension): ") #for part 3 my input was LoanExample
P = input("Please enter the amount of the loan: ")
N = input("Please enter the number of months over which the loan will be repaid: ")
i = input("Please enter the annual interest rate of the loan (as a decimal): ") #takes in all user inputs
try: 
    P = float(P)
    N = float(N) 
    i = float(i) 
except:
    print("Please try again with acceptable inputs.") #makes sure the values are all floats
    raise SystemExit
newFile = open(filename+".csv","w")
newFile.write("Month,Total Interest,Balance\n") #csv header titles
balance = P
J = i/12
M = P*(J/(1-(1+J)**(-N))) #loan calculations
interestTotal = 0
for i in range(int(N)+1):
    newFile.write(str(i)+","+str(interestTotal)+","+str(balance)+"\n") #writing info to new file for every month
    interest = balance*J
    interestTotal += interest
    balance -= M
    balance += interest
newFile.write(str(i+1)+","+str(interestTotal)+","+"0.00"+"\n") #because calculations were done after the write, I had to include an extra write statement for the end.
newFile.close()