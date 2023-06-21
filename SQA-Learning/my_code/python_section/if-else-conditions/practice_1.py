import math
# Underweight - BMI under or equal to 18.5
# Normal - BMI between 18.5 and 25 (not including 18.5 but including 25)
# Overweight - BMI between- 25 and 30 (not including 25 but including 30)
# Obese - BMI greater than 30

weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

bma = weight / (height ** 2)
if bma <= 18.5:
    print(f"Your BMA is equal: {bma} and you Underweight")
elif 18.8 < bma <= 25:
    print(f"Your BMA is equal: {bma} and you Normal")
elif 25 < bma <= 30:
    print(f"Your BMA is equal: {bma} and you Overweight")
else:
    print(f"Your Bma is equal: {bma} and you Obese")
