Item_list = ["sword", "armor", "shield", "healing potion", "gold", "gems"]
Item_list[0] = "crossbow"


print("Press the enter key to continue.")
print("You trade your sword for a crossbow.")
print("Your inventory is now:")
print(Item_list)
print("\n")

print("Press the enter key to continue.")
print("You use your glod and gems to buy an orb of future telling")
print("Your inventory is now:")
del Item_list [4]
del Item_list [4]
Item_list.append("orb of future telling")
print(Item_list)
print("\n")


print("Press the enter key to continue.")
print("In a great battle, your shield is destroyed.")
print("Your inventory is now:")
del Item_list [2]
print(Item_list)
print("\n")

print("Press the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
print("Your inventory is now:")
del Item_list [0]
del Item_list [0]

print(Item_list)
print("\n")
print("\n")

print("Press the enter key to exit.")



