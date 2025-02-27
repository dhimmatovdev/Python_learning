# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Which one L or K ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your something is {weight}")
elif unit == "L":
    weight = weight / 2/205
    unit = "Kgs."
    print(f"Your something is {weight}")
else:
    print(f"{unit} was not valid")
    
