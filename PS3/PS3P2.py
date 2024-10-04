print("Enter price per share")
shareprice = float(input())
print("Enter number of shares")
shares = float(input())
print("Enter stock price")
stockprice = float(input())
value = (stockprice-shareprice)*shares
print(str(value))