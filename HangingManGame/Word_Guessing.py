import random
import time
from TheAnswers import words

answer = random.choice(words).lower()

theWord = ["_"] * len(answer)

wrong_answers = 0

guessed_letters = set()

hanging_man = {
    0: ("   ",
        "   ",
        "   "),
        
    1: (" o ",
        "   ",
        "   "),

    2: (" o ",
        " | ",
        "   "),

    3:  (" o ",
         "/| ",
         "   "),

    4:  (" o ",
         "/|\\",
         "   "),

    5:  (" o ",
         "/|\\",
         "/  "),

    6:  (" o ",
         "/|\\",
         "/ \\"),
}

def show_man(wrong_answers):
    print("*****************************")
    for man in hanging_man[wrong_answers]:
            print(man)
    print("*****************************")

def show_word(theWord):
    for char in theWord:
        print(char, end = " ")
    print()

def main(wrong_answers):
      print("*************")
      print("HANG-MAN GAME")
      print("*************")

      while True:
        show_man(wrong_answers)
        print()
        show_word(theWord)
        choice = input("Guess a Letter in the word: ").lower()

        if len(choice) > 1 or not choice.isalpha():
            print("Invalid guess")
            print()
            time.sleep(1)
            continue
        if choice in guessed_letters:
            print("you already made this guess")
            print()
            time.sleep(1)
            continue

        guessed_letters.add(choice)

        if choice in answer:
            for i in range(len(answer)):
                if answer[i] == choice:
                    theWord[i] = choice
        else:
            wrong_answers += 1
        
        time.sleep(1)
        print()

        if wrong_answers >= len(hanging_man)-1:
            print("game over, you lost")
            show_man(wrong_answers)
            print(f"answer was: {answer}")
            break

        if not "_" in theWord:
            print("You won!!!")
            show_man(wrong_answers)
            print(f"answer was: {answer}")
            break


    
if __name__ == "__main__":
     main(wrong_answers)