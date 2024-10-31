totalpay = 0
counter = 0
loop = input("Would you like to loop? Yes or No")
while loop == "Yes":
  counter+=1
  name = input("Enter employee name")
  hours = int(input("Enter hours worked"))
  payrate = int(input("Enter pay rate"))
  if hours<=40:
    grosspay = hours*payrate
  else:
    grosspay = (40*payrate) + (hours-40)*(payrate*1.5)
  print(f"Employee {name} gross pay is ${grosspay: .2f}")
  totalpay+=grosspay
  print(f"For {counter} employees, Total pay is ${totalpay: .2f}")
  loop = input("Would you like to loop? Yes or No")
averagepay = totalpay/counter
print(f"The average pay is ${averagepay: .2f}")