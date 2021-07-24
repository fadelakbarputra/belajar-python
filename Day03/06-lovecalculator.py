print("Welcome to Love Calculator")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

name1 = name1.lower()
name2 = name2.lower()

# Counting
num_t = name1.count("t") + name2.count("t")
num_r = name1.count("r") + name2.count("r")
num_u = name1.count("u") + name2.count("u")
num_e = name1.count("e") + name2.count("e")
num_l = name1.count("l") + name2.count("l")
num_o = name1.count("o") + name2.count("o")
num_v = name1.count("v") + name2.count("v")
num_e = name1.count("e") + name2.count("e")

# Digit
first_digit = str(num_t + num_r + num_u + num_e)
second_digit = str(num_l + num_o + num_v + num_e )
digit = int(first_digit + second_digit)

# Cek
if digit < 10 or digit > 90:
    print(f"Your score is {digit}, you go like and mentos")
elif digit > 40 and digit < 50:
    print(f"Your score is {digit}, you are allright together")
else:
    print(f"Your score is {digit}")