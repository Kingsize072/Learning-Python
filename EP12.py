#BMI Calculator

#BMI = weight(kg) / height(m)^2

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))/100
bmi = weight / (height ** 2)
print("Your BMI is: ", bmi)