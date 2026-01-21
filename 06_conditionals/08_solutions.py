
user_input = input("Please enter your password: ")
password = user_input.strip()
if len(password) < 8:
    strenth = "Weak"
elif len(password) in range(8, 12):
    strenth = "Medium"
else:
    strenth = "Strong"

print("Your password strength is:", strenth)
