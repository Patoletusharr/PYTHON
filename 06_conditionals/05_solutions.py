user_input = input("How's the waether? (rainy/sunny/Snowy): ")
weather  = user_input.strip().lower()


if weather == "rainy":
    print("Read a book")
elif weather == "sunny":
    print("Go for a walk")
elif weather == "snowy":
    print("Build a snowaman")


# #hitesh example
# if weather == "rainy":
#      activity = "Read a book"
# elif weather == "sunny":
#      activity = "Go for a walk"
# elif weather == "Snowy":
#      activity = "Build a snowaman"
#     print("Today's activity:", activity)

# else:
#     print("Stay home and relax")
