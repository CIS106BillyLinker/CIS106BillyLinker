quantity = int(input("Enter quantity of concert tickets: "))
if quantity>=25:
  price = 50
else:
  if quantity>=10:
    price = 60
  else:
    if quantity>=5:
     price = 70
    else:
     price = 75
totalprice = quantity*price
print(f"The number of tickets is {quantity} The price per ticket is ${price: .2f} The total price is ${totalprice: .2f}")