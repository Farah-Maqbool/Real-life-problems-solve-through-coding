#Recipe calculator
"""Recipe Calculator: Design a recipe calculator that adjusts ingredient quantities based on the 
number of servings. Use variables to store recipe ingredients and amounts, and write 
expressions to calculate adjusted quantities."""
serving=int(input("Number of servings: "))
ing_name=input("Ingredient Name: ")
ing_quantity=int(input("Ingredient Quantity (g): "))
adjust_quantity=ing_quantity/serving
print(f"Take {adjust_quantity} at one time")
