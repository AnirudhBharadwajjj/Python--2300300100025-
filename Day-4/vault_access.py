'''
----------- Secure Vault Access -----------

A digital vault can only be opened if the user enters
the correct security code.

Write a Python program that accepts the entered security
code. If the entered code is 7890, display:

"Access Granted to the Vault."

Otherwise, do nothing.
'''

#------------------------------------------------------
#----------- Coding -----------------------------------

# Input security code from the user
code = int(input("Enter the security code : "))

# Validate security code
if(code < 0):
    exit("Security code must be positive")

#------------------------------------------------------
# Verifying security code

if(code == 7890):

    print("Access Granted to the Vault.")

#------------------------------------------------------

''' Output :

Enter the security code : 7890
Access Granted to the Vault.

'''