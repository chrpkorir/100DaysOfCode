# Enter your height in meters eg 1.6
height = input("Enter your height in meters eg 1.6\n")

# Enter your weight in kilograms eg 60
weight = input("Enter your weight in kilograms eg 60\n")
# Your code below this line

print("------BMI CALCULATOR------")
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print("Your BMI is", bmi_as_int)

"""

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")

elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")

elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")

else:  
  print(f"Your BMI is {bmi}, you are clinically obese.")
"""