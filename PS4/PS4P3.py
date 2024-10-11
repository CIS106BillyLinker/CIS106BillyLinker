bookamount = int(input("Enter the number of books: "))
bookcost = float(input("Enter the cost of each book: "))
totalcost = bookamount*bookcost
shipping = 0 if totalcost>50 else 25
print(f"The total cost is ${totalcost:.2f} and the shipping cost is ${shipping:.2f}")