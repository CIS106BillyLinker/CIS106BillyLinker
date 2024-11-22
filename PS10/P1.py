how_many = int(input("How many numbers do you want to enter? "))
list = []
#1
for i in range(how_many):
  num = int(input("Enter a number: "))
  list.append(num)
print(list)
#2
list.insert(1,99)
print(list)
#3
if 99 in list:
  where=list.index(99)
  list[where]=100
print(list)
#4
list2 = [500,600,700,800,900]
list.extend(list2)
print(list)
#5
list.remove(800)
print(list)
#6
list.pop(2)
print(list)
#7
grades = ["A", "B", "C", "A", "A", "C"]
#8
print("A's: ", grades.count("A"))
#9
print("First B is at position ", grades.index("B"))
#10
if "F" in grades:
  print("F is at position ", grades.index("F"))
else:
  print("F is not in the list")
#11
list2.clear()
print(list2)
#12
del list2
#print(list2)
#13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#14
players.sort()
print(players)
#15
players2 = players.copy()
print(players2)
#16
players2.reverse()
print(players)
print(players2)