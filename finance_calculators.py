import math
print("Welcome")
print("We currently offer the two financial calculators below:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

#take input and ensure lowercase rule

raw_input = input("Enter either 'investment' or 'bond' from the above menu to proceed: ")
choice = raw_input.lower()

#direct user path for either choice (along with calculation)

if choice == "investment":
    ideposit = input("Please enter how much you will be depositing: ")
    irate = input("Please enter your desired interest rate: ")
    itime = input("Please enter your desired number of years: ")
    istyle = input("Please enter 'simple' or 'compound': ")
    interest = istyle.lower()
    r = float(irate)/100
    P = float(ideposit)
    t = int(itime)
    simple = P *(1 + r * t)
    compound = P * math.pow((1+r),t)
elif choice == "bond":
    bvalue = input("Please enter the present value of your property: ")
    brate = input("Please enter your desired interest rate: ")
    btime = input("Please enter the number of months you plan to repay the bond: ")
    i = (float(brate)/100)/12
    P = float(bvalue)
    n = int(btime)
    repay = (i * P)/(1 - (1 + i)**(-n))
    bond = "%.2f" % repay
    print(f"You will have to repay £{bond} each month")
    print("Thank you for using this service")
else:
    print("You have not entered a valid option")

#extension of investment choice (either simple/compound) -add 2 decimal place rule

if choice == "investment" and interest == "simple":
    print("Your expected return is: ")
    print("£%.2f" % simple)
    print("Thank you for using this service")
elif choice == "investment" and interest == "compound":
    print("Your expected return is: ")
    print("£%.2f" % compound)
    print("Thank you for using this service")
elif interest != "simple" or "compound":
    print("You have not entered a valid option")
else:
    pass

#NOTE: 
# I wanted the the above if statement to simply stop the program when it got down to the 'else' statement
# On google I could only find 'pass' as an alternative
#I wanted to also add a further if statement to avoid the user inputting minus numbers at any stage but I struggled to get it working



