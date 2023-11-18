## 트라비아 챌린지_Trivia Challenge 1.py
import sys

def open_file(file_name, mode):
    """open a file"""
    try:
        the_file = open(file_name, mode)
    except IOError as error:
        print("Unable to open the file", file_name, "Ending program. \n", error)
        input("Press Enter key to exit")
        sys.exit()
    else:
        return the_file
# 단순히 파일을 읽어온다.

def next_line(the_file):
    """Return the next line from the trivia file, formatted"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
# 파일에서 다음 줄을 반환하고, 형식을 지정한다.

def next_block(the_file):
    """Return the next block of data from the trivia file"""
    category = next_line(the_file)

    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    points = next_line(the_file)
    if correct:
        correct = correct[0]  # 여기서 "correct"를 리스트로 받아서 [0]번째 요소를 사용

    explanation = next_line(the_file)
    return category, question, answers, correct, points, explanation
# 트라비아 파일에서 다음 블록의 데이터를 반환한다. (카테고리별)

def welcome(title):
    """Welcome the player, get his/her name"""
    print("\t\tWelcome to Trivia Challenge\n")  # 오타 수정
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("thefileedit.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t-", i + 1, answers[i])  # "answer" 대신 "answers" 사용

        answer = input("What's your answer?:\t")
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)

        else:
            print("\nWrong!", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        print("Possible amount of points from question:\t", points)

        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("\nThat was the last question!")  # "That" 오타 수정
    print("\nYour final score is", score)

main()
input("Press Enter to exit")

