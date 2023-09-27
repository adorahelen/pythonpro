print(" I sense your energy. Your true emotions are coming across my screen.")
print(" You are ...") 

mood  = int(input())

if mood == 0:
    print("-----------------")
    print("|               |")
    print("|    0     0    |")
    print("|      <        |")
    print("|   =       =   |")
    print("|    (     )    |")
    print("|     _ _ _     |")
    print("-----------------")
    # happy

elif mood == 1:
    print("-----------------")
    print("|               |")
    print("|               |")
    print("|   (*)    (*)  |")
    print("|       Y       |")
    print("|               |")
    print("|   -MMMMMMM-   |")
    print("-----------------")
    # angry


elif mood == 2:
    print("-----------------")
    print("|               |")
    print("|    (&)  (&)   |")
    print("|     *    *    |")
    print("|     *    *    |")
    print("|     *    *    |")
    print("|               |")
    print("|     [UUU]     |")
    print("-----------------")
    #sad

else: 
    print ("Illegal mood value!")

print("... today.")
print(" " )
print("Press the enter key to quit.")
