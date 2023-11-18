input ("Opening and Closing the file")
text_file = open ("read_it.txt", "r") #읽기 형식으로 r
text_file.close() #파일을 닫지 않으면 문제

input ("\n Reading character from the file: \t") 
text_file = open ("read_it.txt", "r")
print (text_file.read(1))
print (text_file.read(5))
text_file.close ()

input ("\n Reading the entire file at once")

text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print (whole_thing)
text_file.close ()

input ("\n Reading one line at a time")
text_file = open ("read_it.txt", "r")
print (text_file.readline ())
print (text_file.readline ())
print (text_file.readline ())
text_file.close () 

input ("\n Reading characters from a line")
text_file = open("read_it.txt", "r")
print (text_file.readline (1))
print (text_file.readline (5))
text_file.close () 

input ("Reading the entire file onto a list")
text_file = open ("read_it.txt", "r")
lines = text_file.readlines ()
print (lines)
print (len(lines))
for line in lines : 
 print (line) 
text_file.close ()

input ("\n Looping through the file, line by line")

text_file = open ("read_it.txt", "r")
for line in text_file: 
 print (line)


