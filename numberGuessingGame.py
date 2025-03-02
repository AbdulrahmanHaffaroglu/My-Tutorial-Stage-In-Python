import random

number = random.randint(1, 100)

guessed_number = input("choose a number between 0-100: ")

guesses = 0

while True:
    if not guessed_number.isdigit():
       guessed_number = input("you should choose a number: ")
    elif int(guessed_number) < 0 or int(guessed_number) > 100:
       guessed_number = input("you should choose between 0-100: ")
    elif int(guessed_number) < number:
       guessed_number = input("too low, try again:")
       guesses += 1
    elif int(guessed_number) > number:
       guessed_number = input("too high, try again:")
       guesses += 1
    elif number == int(guessed_number):
        print("congratulations, you found the correct answer")
        guesses += 1
        break

print(f"it took you {guesses} guesses")