with open("students.txt", "w") as file:
    file.write("Smith,I,12\n")
    file.write("Johnson,O,10\n")
    file.write("Williams,I,15\n")
    file.write("Brown,O,8\n")
    file.write("Jones,I,18\n")
INDISTRICTCOST = 250.00
OUTOFDISTRICTCOST = 500.00
totaltuition = 0
studentcount = 0
with open("students.txt", "r") as file:
    for line in file:
        lastname, districtcode, creditstaken = line.split(",")
        creditstaken = int(creditstaken)  

        if districtcode == "I":
            costpercredit = INDISTRICTCOST
        elif districtcode == "O":
            costpercredit = OUTOFDISTRICTCOST
       
        tuitionowed = creditstaken * costpercredit
        totaltuition += tuitionowed  
        studentcount += 1 
        print(f"Name: {lastname} Credits: {creditstaken} Tuition: ${tuitionowed:.2f}")


print(f"Total tuition owed: ${totaltuition:.2f}")
print(f"Number of students: {studentcount}")
