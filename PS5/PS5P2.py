item = input("Enter items to be purchased : ")
quantity = int(input("Enter quantity : "))
if item == "10" or item == "55":
  unitprice = 1.00
else:
  if item == "99":
    unitprice = 2.00
  else:
    if item == "80" or item == "70":
      unitprice = 3.00
    else:
      unitprice = 5.00
price = quantity*unitprice
print(f"You ordered part {item} The unit price is ${unitprice: .2f} The extended price is ${price: .2f}")