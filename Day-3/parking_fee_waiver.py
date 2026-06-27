'''
----------- Parking Fee Waiver -----------

A shopping mall waives the parking fee if a customer
has made purchases worth ₹2000 or more.
Otherwise, the customer must pay a parking fee of ₹100.

Write a Python program to accept the purchase amount
and display whether the parking fee is waived or payable.
'''

#------------------------------------------------------
#----------- Coding -----------------------------------

# Input purchase amount from the user
purchase = float(input("Enter the purchase amount: "))

# Validate purchase amount
if(purchase < 0):
    exit("Purchase amount must be positive")

#------------------------------------------------------
# Verifying parking fee eligibility

if(purchase >= 2000):
    parking_fee = 0

    print("Parking Fee Waived!")
    print(f"Parking Fee: ₹{parking_fee}")

else:
    parking_fee = 100

    print("Parking Fee Applicable!")
    print(f"Parking Fee: ₹{parking_fee}")

#------------------------------------------------------

''' Output :

Enter the purchase amount: 2500
Parking Fee Waived!
Parking Fee: ₹0

'''