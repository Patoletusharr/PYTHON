distance = input("Enter the distance you want to travel (in km): ")
distance = float(distance)

if distance < 3:
    mode = "Walk"
elif distance >= 3 and distance <= 15:
    mode = "Bike"
elif distance > 15:
    mode = "Car"

print("You should travel by:", mode)