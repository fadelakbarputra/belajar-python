print("Welcome to Pizza Delivers!")
bill = 0
size = input("Mau ukuran apa S, M, L? ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
papperoni = input("Mau papperoni Y or N? ")
if papperoni == "Y":
    if size == "S":
        bill += 2
    else: 
        bill += 3
cheese = input("Mau ekstra keju Y or N? ")
if cheese == "Y":
    bill += 1
print(f"Your final bill is ${bill}")