def getpayrate(jobcode):
    jobrates = {'L': 25, 'A': 30, 'J': 50}  
    return jobrates.get(jobcode.upper(), 0)  

totalgrosspay = 0  
employees = []      

while True:
  
    lastname = input("Enter employee's last name: ")
    jobcode = input("Enter job code (L, A, J): ")
    hoursworked = float(input("Enter hours worked: "))

  
    payrate = getpayrate(jobcode)

    if payrate == 0:
        print("Invalid job code. Please try again.")
        continue

   
    if hoursworked > 40:
        overtimehours = hoursworked - 40
        grosspay = (40 * payrate) + (overtimehours * payrate * 1.5)
    else:
        grosspay = hoursworked * payrate

    employees.append((lastname, grosspay))

    totalgrosspay += grosspay

    moreemployees = input("Do you want to enter another employee? (yes/no): ").lower()
    if moreemployees != "yes":
        break


print(f"Last Name: {lastname} and Gross Pay: ${grosspay:.2f}")
print(f"Total Gross Pay: ${totalgrosspay:.2f}")