input_tuple = tuple()
count = 0

for i in range(4):
    ItemName = input()
    input_tuple += (ItemName,)
    count += 1

print("")
print("")
print("Your items:")

for item in input_tuple:
    print(item)
print("")

print("Press the enter key to continue.")
print("You have %d item in your possession.\n" % count)


print("Press the enter key to continue.")
postion = "healing potion"
if "potion" in ItemName:
    print("You will live to fight another day.\n")


input_call= int(input("Enter the index number for an item in iventory: "))
if input_call == 0:
    print("At index 0 is", input_tuple[0]) 
elif input_call == 1:
    print("At index 1 is", input_tuple[1]) 
elif input_call ==2:
    print("At index 2 is", input_tuple[2])
elif input_call ==3:
    print("At index 3 is", input_tuple[3]) 

print("")
input_slice1 = int(input("Enter the index number to begin a slice: "))
input_slice2 = int(input("Enter the index number to begin a slice: "))

result = ("inventory [%d : %d] " % (input_slice1, input_slice2))
result2 ="', '".join(input_tuple[input_slice1 : input_slice2])
output = result+ "     <'" +result2 + "'>"
print(output)
print("")

print("Press the enter key to continue.")

print("You find a chest. it contains:")


chest_tuple = ('gold', 'gems')
# result = ",".join(chest_tuple)
result_str = "', '".join(chest_tuple)
result_str = "<'" + result_str + "'>"

print(result_str)
print("You add the contents of the chest to your inventory.")
print("Your inventory is now:")
inventory = input_tuple + chest_tuple

# inventory_str = ",".join(inventory)
inventory_str = "', '".join(inventory)
inventory_str = "<'" + inventory_str + "'>"
print(inventory_str)



# ending = input_tuple + chest_tuple   
# lastending = ",".join(ending)
# realending = "<%s>" %lastending
# print(realending)

print("")
print("Press the enter key to exit.")
