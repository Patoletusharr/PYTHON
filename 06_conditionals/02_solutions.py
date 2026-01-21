age = 18
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2
    # price-=2 # This is another way to write the same operation
print("Ticket price for you is $",price)