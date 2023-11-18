print ("\nCreating a text file with the write() method!")

text_file = open ("read_this.txt", "w")
text_file.write ("Line 1\n")
text_file.write ("This is line 2\n")
text_file.write ("That makes this line 3\n")
# 파일을 쓰기 모드로 open 후 write 메서드로 파일 쓰기 작업
text_file.close ()

# 사용자가 Enter 키를 누를때까지 기다린 후 읽기,출력 진행
input ("\nReading the newly created file")

text_file = open ("read_this.txt", "r")
print (text_file.read())
print ("\n And that would make this the third line.")

input ("\nCreating a text file, with the writelines () method")

# 파일을 읽어와 라인 단위로 쓰기를 진행한다. 
text_file = open ("read_this.txt", "w")
# creating list
lines = ["Line 1 \n",
         "This is line 2\n",
         "That makes this line 3\n"]
text_file.writelines(lines)


text_file.close ()

print ("\nReading the newly created file")


text_file = open ('read_this.txt', 'r')


print (text_file.read())

input ("\nPress Enter key to exit")
