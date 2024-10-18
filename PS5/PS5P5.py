lastname = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
joblevel = int(input("Enter job level: "))
if joblevel>=10:
  bonusrate = 0.25
else:
  if joblevel>=5:
    bonusrate = 0.2
  else:
    bonusrate = 0.1
bonus = salary*bonusrate
print(f"The last name of the employee is {lastname} The bonus is ${bonus: .2f}")