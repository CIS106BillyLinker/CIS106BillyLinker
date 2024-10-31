loop = input("Do you want to loop")
counter = 0
while loop == "yes":
  name = input("Enter your name")
  midterm = int(input("Enter your midterm grade"))
  final = int(input("Enter your final grade"))
  average = (midterm + final) / 2
  counter+=1
  print(name, "your average is", average)
  loop = input("Do you want to loop")
print("you looped " + str(counter) + " times")