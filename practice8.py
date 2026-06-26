# manging an fruitshop
fruitshop=["apple","banana","watermelon","orange","grapes"]

# adding a new item
fruitshop.append("strawbarries")

# removing an iems
fruitshop.remove("banana")

# checking if an item is in stock
item="orange"
if item in fruitshop:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of shock.")
    
#printing the fruitshop
print("fruitshop list:")
for item in fruitshop:
    print(f"-{item}")
    
    
