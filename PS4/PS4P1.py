quantity = float(input("Enter quantity: "))
price = 3 if quantity >= 1000 else 5 
extendedprice = quantity*price
tax = 0.07*extendedprice
totalprice = extendedprice+tax
print(f"The total price is $ {totalprice: .2f}")
