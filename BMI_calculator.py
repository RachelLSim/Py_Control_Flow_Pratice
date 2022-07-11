height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_calc = weight / height ** 2

bmi = round(bmi_calc, 2)

if bmi < 18.5:
    print(f"Your BMI is under 18.5 at {bmi} You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
else: 
    print(f"Your BMI is {bmi}. You are clinically obese.")