# file name 명시
file_name = "writeANDread.txt"

#입력받아 파일에 쓰기
with open(file_name, "w") as file:

	while True:
		user_input = input("input some String(if == Q :end)")
		if user_input.upper() == "Q":
			break
		file.write(user_input + '\n')

#쓰여진 파일 내용 읽어서 출렷
#무조건 읽어야지 출력 가능함!

with open (file_name, "r") as file:
 content = file.read() 
 print("\n <content of files>")
 print(content)
