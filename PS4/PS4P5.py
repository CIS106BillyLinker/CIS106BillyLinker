lastname = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
grossincome = float(input("Enter gross income: "))
adjustedgrossincome = grossincome - dependents*12000
incometaxrate = 0.2 if adjustedgrossincome > 50000 else 0.1
incometax = adjustedgrossincome*incometaxrate 
if incometax < 0:
  incometax = 100
print(f"Last name: {lastname} Number of dependents: {dependents} Gross income: ${grossincome: .2f} Adjusted gross income: ${adjustedgrossincome: .2f} IncomeTax: ${incometax: .2f}")
