print("Program menghitung BMI: ")
weight = float(input("Input your weight in kg: "))
height = float(input("Input your height in m: "))

bmi = round(weight / (height ** 2))
# elif akan jalan jika dan hanya jika yang atasnya false
if bmi < 18.5:
    print(f"Your bmi is {bmi}, underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, obese")
else:
    print(f"Your bmi is {bmi}, clinically obese")