def computetuition(credithours, districtcode):
    if districtcode.upper() == "I":
        return credithours * 250  
    elif districtcode.upper() == "O":
        return credithours * 550  
    else:
        return None  


totaltuition = 0  
students = []     


while True:
  
    lastname = input("Enter student's last name: ")
    credithours = int(input("Enter credit hours: "))
    districtcode = input("Enter district code (I/O): ")

  
    tuition = computetuition(credithours, districtcode)

    if tuition is None:
        print("Invalid district code. Please try again.")
        continue

   
    students.append((lastname, tuition))

    
    totaltuition += tuition

   
    morestudents = input("Do you want to enter another student? (yes/no): ").strip().lower()
    if morestudents != "yes":
        break


for student in students:
    print(f"Name: {student[0]}  Tuition: ${student[1]:.2f}")

print(f"Total Tuition Owed: ${totaltuition:,.2f}")
