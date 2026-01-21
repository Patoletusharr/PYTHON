raw_score = input("Please enter your score to know your Grade")
score = int(raw_score)

if score < 0 or score > 100:
    print("Invalid score")
    exit()
if score in range(90, 101): #101 because the upper bound is exclusive in range()
    print("Grade A")
elif score in range(80, 90): 
    print("Grade B")
elif score in range(70, 80):
    print("Grade C")
elif score in range(60, 70):
    print("Grade D")
else:
    print("Grade F")


# score = 95

# if 90 <= score <= 100:
#     print("Grade A")
# elif 80 <= score <= 89:
#     print("Grade B")
# elif 70 <= score <= 79:
#     print("Grade C")
# elif 60 <= score <= 69:
#     print("Grade D")
# else:
#     print("Grade F")
