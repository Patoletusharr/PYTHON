# food_type = "Puppy Food"
pet_type = "Cat"
age = 6

if pet_type == "Dog" and age <= 2:
    suggested_food = "Puppy Food"
elif pet_type == "Cat" and age >= 5:
    suggested_food = "Senior Cat Food"

print("for your",pet_type, f"{suggested_food} is the best option")

Question was: recommend a type of food based on the pets species and age.eg Dog: <2 years = Puppy Food, Cat: >5 years = Senior Cat Food

pet_type = "cat"
age = 6

pet_type = pet_type.lower()

if pet_type == "dog" and age < 2:
    suggested_food = "Puppy Food"
elif pet_type == "cat" and age > 5:
    suggested_food = "Senior Cat Food"
else:
    suggested_food = "Regular Pet Food"

print(f"For your {pet_type}, {suggested_food} is the best option.")
