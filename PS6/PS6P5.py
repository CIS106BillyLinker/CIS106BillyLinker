discounttotal = 0
counter = 0
loop = input("Would you like to loop? Yes or No")
while loop == "Yes":
  counter+=1
  quantity = int(input("Enter quantity"))
  price = float(input("Enter price"))
  extendedprice = quantity*price
  if extendedprice>10000.00:
    discount = 0.25
  else:
    discount = 0.1
  discountamount = extendedprice*discount
  total = extendedprice - discountamount
  print(f"Extended price is ${extendedprice: .2f} discount amount is ${discountamount: .2f} and total is ${total: .2f}")
  discounttotal+=discountamount
  print(f"For {counter} orders, total discount is ${discounttotal: .2f}")
  loop = input("Would you like to loop? Yes or No")