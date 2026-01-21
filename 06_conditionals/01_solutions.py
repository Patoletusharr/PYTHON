raw_age_input = input("Please enter your age: ")

age = int(raw_age_input)
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")