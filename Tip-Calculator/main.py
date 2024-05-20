print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n")) / 100
people = int(input("How many people to split the bill?\n"))
print("Each person should pay: $ %.2f"%((bill/people)*(1+tip)))
