#Code to check if the given number is a natural number or not
#input of number from user
number = int(input("Enter a number : "))
#to validate number of the customer
if(number <= 0):
    exit("Number must be positive")
#---------------------------------------------------
#verifying if the number is a natural number or not     
if(number >= 1 ):
    print("The given number is a natural number")
else:
    print("The given number is not a natural number")
