# 1) Ask the user to enter their height in centimeters and store it in `height`.

# 2) Ask the user to enter their weight in kilograms and store it in `weight`.

# 3) Calculate BMI using the formula:

# BMI = weight ÷ (height in meters)²

# (Convert height from cm to meters by dividing by 100.)

# Store the result in `BMI`.

# 4) Print the BMI value.

# 5) Use if–elif–else to decide the BMI category:

# - If BMI is 18.4 or less → print "underweight"

# - Else if BMI is 24.9 or less → print "healthy"

# - Else if BMI is 29.9 or less → print "over weight"

# - Else if BMI is 34.9 or less → print "severely over weight"

# - Else if BMI is 39.9 or less → print "obese"

# - Else → print "severely obese"
height=int(input("Enter your height in centimeters: "))
weight=float(input("Enter you weight in kilograms: "))
hm=height/100
bmi=weight/hm**2
print("Your BMI is:",round(bmi,2))
if bmi<=18.4:
    print("You are underweight")
elif bmi<=24.9:
    print("You are healthy")
elif bmi<=29.9:
    print("You are over weight")
elif bmi<=34.9:
    print("You are severly over weight")
elif bmi<=39.9:
    print("You are obese")
else:
    print("You are everly obese")