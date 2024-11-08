with open("items.txt", "w") as file:
    file.write("Pen,10,1.50\n")
    file.write("Notebook,5,3.00\n")
    file.write("Eraser,20,5.00\n")
    file.write("Marker,8,2.00\n")
    file.write("Ruler,15,10.00\n")
totalextendedprice = 0
ordercount = 0
with open("items.txt", "r") as file:
    for line in file:
        item, quantity, price = line.split(",")
        quantity = int(quantity)  
        price = float(price)
        extendedprice = quantity * price
        totalextendedprice += extendedprice  
        ordercount += 1  
        print(f"Item: {item} Quantity: {quantity} Price: ${price:.2f}  Extended Price: ${extendedprice:.2f}")

averageorder = totalextendedprice / ordercount

print("-" * 45)
print(f"Total extended price: ${totalextendedprice:.2f}")
print(f"Number of orders: {ordercount}")
print(f"Average order amount: ${averageorder:.2f}")
