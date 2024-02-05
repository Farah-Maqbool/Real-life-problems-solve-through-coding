# Hostel bill (practical 3)
item_price={}
while True:
    item=input("Item name: ")
    price=int(input(f"Price of {item}: "))
    item_price[item]=price
    if input("Do you want to continue (y or n): ")=="n":
        break
sum=0
for key, val in item_price.items():
    sum+=val
print(f"Total bill {sum}")