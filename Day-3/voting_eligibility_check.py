#'''----------  Voting Eligibility check ------------------
#input of age from user
age = int(input("Enter age(in year) : "))
#to validate age of the customer
if(age <= 0):
    exit("Age must be positive")
#---------------------------------------------------
#verifying eligibility of the customer
if(age >= 18 ):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")