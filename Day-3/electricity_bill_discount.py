"""
---------- Electricity Bill Discount ----------

An electricity provider offers a 10% discount on the total bill
amount if the customer's bill is ₹5000 or more.
Otherwise, no discount is applied.
"""

# Input bill amount from user
bill = float(input("Enter the electricity bill amount: "))

# Validate the bill amount
if bill < 0:
    exit("Bill amount cannot be negative")

# Check eligibility for discount
if bill >= 5000:
    discount = bill * 0.10
    final_bill = bill - discount

    print("Discount Applied!")
    print(f"Final Bill Amount: ₹{final_bill}")

else:
    final_bill = bill

    print("No Discount Applied!")
    print(f"Final Bill Amount: ₹{final_bill}")