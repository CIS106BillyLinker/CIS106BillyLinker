with open("employees.txt", "w") as file:
    file.write("Smith,48000\n")
    file.write("Johnson,75000\n")
    file.write("Williams,102000\n")
    file.write("Brown,45000\n")
    file.write("Jones,56000\n")
totalbonus = 0
with open("employees.txt", "r") as file:
    for line in file:
        lastname, salary = line.split(",")
        salary = float(salary)
        if salary < 50000:
            bonusrate = 0.05
        elif 50000 <= salary <= 100000:
            bonusrate = 0.10
        else:
            bonusrate = 0.15
        bonus = salary * bonusrate
        totalbonus += bonus  
        print(f"Name: {lastname}  Salary: ${salary:.2f} Bonus: ${bonus:.2f}")
print(f"Total bonuses paid out: ${totalbonus:.2f}")
