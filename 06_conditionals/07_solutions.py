order_size = "medium"
extra_shot = False

if extra_shot:  #if extra_shot == True:
    coffee = order_size + " coffee with an extra expresso shot"
else:
    coffee = order_size + " coffee"
print("Order:", coffee)