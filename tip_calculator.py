print("Let's figure out your bill, shall we?") 
print("")
bill = float(input("What was the food cost? Example: 20.95. "))
tip = 1.20
tax_percentage = 1.0825
bill_tax = bill*tax_percentage
print("")
print(f"Your with tax: {bill_tax}")
total = bill_tax * tip
print("")
print(f"Your total (w/tax and tip) is: {total}.")