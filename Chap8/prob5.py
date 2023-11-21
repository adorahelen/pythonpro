# 기본적인 예외처리 
try:
    num = float(input("Enter a number:\t"))
except:
    print ("Something went wrong!")

# 특정 예외 타입 처리 
try:
    num = float(input("Enter a number:\t"))
except ValueError:
    print ("That was not a number")

# 다중 예외 처리 

print ()
for value in (None, "Hi!"):   
    try:
        print ("Attempting to convert", value, "--->", end = " ")
        print (float(value))
    except (ValueError, TypeError):
        print ("Something went wrong!")

# 다중 예외에 대한 구체적인 처리 
print ()

for value in (None, "Hi!"):
    try:
        print ("Attempting to convert", value, "--->", end = " ")
        print (float(value))
    # first except clause
    except ValueError:
        print ("I can only convert a string of digits!\t")
    # second except clause
    except TypeError:
        print ("I can only convert a string or a number!\t")

# 수정해야 화는 부분 
try:
    num = float(input("\nEnter a number:\t"))
except(ValueError) as e:
	print ("That was not a number! Or as Python would say:\t", e, sep = '')
try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!") 
else:
 	print ("You entered the number \t", num)

input ("\n\nPress Enter key to exit")
