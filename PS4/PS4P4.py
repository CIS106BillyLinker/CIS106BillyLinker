appliancename = input("Enter the name of the appliance: ")
appliancecost = float(input("Enter the cost of the appliance: "))
warrantee = 0.1*appliancecost if appliancecost > 1000 else 0.05*appliancecost
total = appliancecost+warrantee
print(f"The name of the appliance is {appliancename} The cost of the appliance is ${appliancecost:.2f} The warrantee is ${warrantee: .2f} The total is ${total:.2f}")
