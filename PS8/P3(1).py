def computempg(miles, gallons):
    return miles / gallons
tripcount = 0

moretrips = input("Do you want to enter another trip? (yes/no): ")
while moretrips == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = computempg(miles, gallons)

    tripcount += 1

    print("Destination: ", city, "Miles: ",miles, "Gallons: ", gallons, "MPG: ", mpg)
    
    moretrips = input("Do you want to enter another trip? (yes/no): ")

print(f"Total number of trips: {tripcount}")
