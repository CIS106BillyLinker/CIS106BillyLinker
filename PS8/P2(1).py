def calculatebattingaverage(hits,atbats):
  batavg=hits/atbats
  return batavg


for count in range(1,10,1):
  name=input("Enter the player's name ")
  hits=int(input("Enter the number of hits "))
  atbats=int(input("Enter the number of at bats "))
  batavg=calculatebattingaverage(hits,atbats)
  print("Player: ", name, "Batting Average: ", batavg)
print("9 Players Entered")