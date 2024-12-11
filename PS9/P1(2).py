def display(names):
  for i in names:
    print(i)
def reverse(names):
  for i in range(len(names)-1,-1,-1):
    print(names[i])


names=["Bob" , "Jane" , "Mary" , "Jim", "John", "Jack", "Jill", "Jessica", "Jess", "Jessica"]

display(names)
print()
reverse(names)