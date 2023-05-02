#BMI Program

name = input("Welcome! What's your name? ")
print("")
print(f"Thanks, {name}! ")
print("")
user_weight = int(input("Please input your weight: "))
user_height = int(input("Please input your height: "))
bmi = user_weight / (user_height**2)*703
print(bmi)
print("")

if bmi < 18.5:
	print("You are underweight.")
elif bmi < 25:
	print("Congrats! You're normal!")
elif bmi < 30:
	print("You are overweight.")
if bmi >= 30:
	print("You are CHONKY. Obese.")


# practice: user_weight = 118.278
# practice: user_height = 61