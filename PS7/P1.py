loop = input("Would you like to loop? Yes or No")
while loop == "Yes":
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate "))
    accumulatedinterest = 0  
    beginningbalance = principal
    for year in range(1, 6):
        interest = beginningbalance * rate
        endingbalance = beginningbalance + interest
        accumulatedinterest += interest

        print(f"year: {year}  Beginning Balance: ${beginningbalance:.2f} interest: ${interest:.2f} endingbalance: ${endingbalance:.2f}")

        beginningbalance = endingbalance

    print(f"Total accumulated interest over 5 years: ${accumulatedinterest:.2f}")
    loop = input("Would you like to loop? Yes or No")
   