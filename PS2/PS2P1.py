print ("Enter a Stock Symbol")
stock = input()
print ("Enter the number of shares")
shares = float(input())
print ("Enter the price per share")
price = float(input())
cost= shares*price
print ("The cost of the stock " + stock + " is $" + str(cost))
