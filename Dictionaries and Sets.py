#creating dictionaries

menu = {
      "burger": 7.99,
      "pizza" : 10.49,
      "salad" : 5.99,
      "soda"  : 1.59,
      "soda"  : 1.79
}
print("Menu : ", menu)

#accessing values with keys
print("Burger Pricce:", menu["burger"])
print("Soda Price:", menu["soda"])

#add and modify dictionaries
menu["fries"] = 3.99
print("Updated Menu:", menu)
menu["Salad"] = 6.99
print("Salad Update", menu)        

#remove from dictionaries
removed_item = menu.pop("salad")
print("Menu after salad removal:", menu)
print("Price of salad : ", removed_item)

#common dictionary method
print("Menu Items : ", list(menu.keys()))
print("Item Prices : ", list(menu.values()))
print("All items and prices", menu.items())

#checking if a key exists
if "pizza" in menu:
    print("Pizza is a key")

for key, value in menu.items():
    print("Menu Item", key, ":", value)  

#creating sets

colors = {"Red", "Blue", "Purple", "Red", "Green", "Red", "Red"} 
print(colors)

colors.add("Brown")
print("Adding brown : ", colors)

colors.remove("Blue")
print("Removing Blue : ", colors)

#removing duplicates
numbers = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
unique_nums = set(numbers)
print("Unique Numbers:", unique_nums)

#set operators
set_a = {1, 2, 3, 4, 5, 6, 7}
set_b = {3, 4, 5, 6, 7, 8, 9}
print("Union", set_a | set_b)
print("Intersection", set_a & set_b)
print("Difference", set_a - set_b)