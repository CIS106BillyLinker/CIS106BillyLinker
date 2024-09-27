print ("Enter Make")
make = input()
print ("Enter Model")
model = input()
print ("Enter msrp ")
msrp = float(input())
print ("Enter Discount")
discount = float(input())
amountdiscounted = msrp * discount
finalcost = msrp - amountdiscounted
print ("The make is " + make + " the model is " + model + " the msrp is " + str(msrp) + " the discount is " + str(discount) + " the amount discounted is " + str(amountdiscounted) + " the final cost is " + str(finalcost))