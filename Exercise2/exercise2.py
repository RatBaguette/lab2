def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    height = float(height)
    weight = float(weight)
    bmi = float(weight/(height*height))
    return bmi


bmi = calculate_bmi(weight=57, height=1.73)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 25.0:
    print("Normal Weight")
else:
    print("Overweight")