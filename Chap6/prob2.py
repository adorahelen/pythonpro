default_list = {}
compare_list = {"Moe" : 1000}, {"lary" : 1500}

def get_value(item):
  return item[1]

while 1:
    print("\tHigh Scores Keeper")
    print ("\n")
    print("\t0 - Quit")
    print("\t1 - List Score")
    print("\t2 - Add a Score")
    print ("\n")
    choice = int(input("Choice: "))

    if choice == 0:
        break
    elif choice == 2:
        name = str(input("What is the player's name?:"))
        score = int(input("What score did the player get?:"))
        print("\n")

        default_list[name] = score
        combined_dict = {**default_list, **compare_list}
        sorted_dict = dict(sorted(combined_dict.items(), key=get_value))

    elif choice == 1:
        print(sorted_dict)






