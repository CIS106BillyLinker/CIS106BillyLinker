mealcost = float(input("Enter the cost of the meal: "))
tip1 = mealcost * 0.15
tip2 = mealcost * 0.18
tip3 = mealcost * 0.20
total1 = mealcost + tip1
total2 = mealcost + tip2
total3 = mealcost + tip3
print(f"With 15% Tip:\n Total: $ {mealcost:.2f}\n Tip: $ {tip1:.2f}\n Total with Tip: $ {total1:.2f}")
print(f"With 18% Tip:\n Total: $ {mealcost:.2f}\n Tip: $ {tip2:.2f}\n Total with Tip: $ {total2:.2f}")
print(f"With 20% Tip:\n Total: $ {mealcost:.2f}\n Tip: $ {tip3:.2f}\n Total with Tip: $ {total3:.2f}")