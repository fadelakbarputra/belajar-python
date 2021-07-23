print("Welcome to the tips calculator!")
total = float(input("What was the total bill? $ "))
percen = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_each_people = round((total / people) + (total * (percen/100) / people), 2)
print(f"Each person should pay {bill_each_people}")
