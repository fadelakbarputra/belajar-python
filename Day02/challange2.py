print("Program menghitung BMI: ")
weight = int(input("Input your weight in kg: "))
height = float(input("Input your height in m: "))

bmi = weight / (height ** 2)
print(int(bmi))
