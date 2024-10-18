quantity = int(input("Enter quantity of widgets: "))
if quantity>10000:
  price = 10
else:
  if quantity>5000:
    price = 20
  else:
    price=30
extendedprice = quantity*price
taxamount = 0.07*extendedprice
totalprice = extendedprice+taxamount
print(f"The extended price is ${extendedprice: .2f} and the tax amount is ${taxamount: .2f} and the total price is ${totalprice: .2f}")