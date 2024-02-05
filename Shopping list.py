#Shopping list.
"""Shopping List: Write a program to manage a shopping list. Use variables to store item names, 
quantities, and prices. Calculate the total cost of items and check if you have enough budget"""
budget=int(input("Budeget: "))
total_cost=0
while True:
    item_names=input("Item names: ")
    price=int(input("Price: "))
    quantity=int(input("Quantity: "))
    sum=price*quantity
    total_cost+=sum
    if input("Do you want continue (yes or no): ")=="no":
        break
if total_cost<budget:
    print(f"you have {budget-total_cost} rupees left")
else:
    print("You have not enough budget")
