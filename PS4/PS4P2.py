item = input("Enter item A or B: ")
quantity = int(input("Enter quantity: "))
unitprice = 10 if item == "A" else 20
extendedprice = quantity*unitprice
print(f"You chose Item {item} The UnitPrice is ${unitprice: .2f} The extended price is ${extendedprice: .2f}")