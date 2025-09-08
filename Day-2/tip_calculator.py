# Day 2 Project: Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * tip / 100
total = bill + tip_amount
split = total / people
print(f"Each person should pay: ${split:.2f}")