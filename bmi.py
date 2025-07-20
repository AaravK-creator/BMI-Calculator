weight = float(input("Enter your weigth in kgs: "))
height = float(input("Enter your height in cm: "))

heightm = height/100
height1 = heightm*heightm

bmi=weight/height1

print(bmi)

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 < bmi < 25.9:
    print("You are Healthyweight")
elif 25 < bmi < 29.9:
    print("You are Overweight")
elif bmi > 30:
    print("You are Obese")