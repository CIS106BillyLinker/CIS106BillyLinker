def calculatetotal(quantity,price):
  total=quantity*price
  if total>10000:
    total=total*0.9
  return total

eprice=0
loop = input("Would you like to loop? Yes or No")
while loop == "Yes":
  quantity = int(input("Enter the quantity "))
  price = float(input("Enter the price "))
  totalcost = calculatetotal(quantity,price)
  print("Quantity Purcahsed ", quantity, "Price per unit $", "{:.2f}".format(price), "Total cost is $", "{:.2f}".format(totalcost))
  eprice=eprice+totalcost
  loop = input("Would you like to loop? Yes or No")
print("Total of all entries $", "{:.2f}".format(eprice))