principle = int(input("Enter the principle amount: "))
years = int(input("Enter the years to maturity: "))
if principle>100000 and years==5:
  interest = 0.06
else:
  if principle>50000 and years==10:
    interest = 0.05
  else:
    if principle>50000 and years==5:
      interest = 0.04
    else:
      interest = 0.02
firstyearinterest = principle*interest
print(f"The principle is ${principle: .2f} The interest rate is %{100*interest} The interest amount for the first year is ${firstyearinterest: .2f}")