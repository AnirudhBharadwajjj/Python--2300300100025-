'''
----------- Scholarship Eligibility -----------

A university provides a scholarship only to students
who score 90 or above.

If percentage is 90 or above:
Scholarship Approved

Otherwise:
Scholarship Not Approved
'''

#------------------------------------------------------
#----------- Coding -----------------------------------

percentage = float(input("Enter percentage : "))

if(percentage < 0 or percentage > 100):
    exit("Invalid percentage")

if(percentage >= 90):
    print("Scholarship Approved")
else:
    print("Scholarship Not Approved")

#------------------------------------------------------

''' Output :

Enter percentage : 92
Scholarship Approved

'''