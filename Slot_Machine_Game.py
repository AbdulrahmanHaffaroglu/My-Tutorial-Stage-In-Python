import random
import time

def spin():
    signs = ['🍒', '🍉', '🍋', '🔥', '🌟']
    print("Spinning...")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    result = [random.choice(signs) for sign in range(3)]
    return result

def print_row(result):
    print()
    print(*result, sep="|")

def payout(result, bet):
    if result[0] == result[1] == result[2]:
        match result[0]:
            case "🍒":
                return bet * 1.5
            case "🍉":
                return bet * 3
            case "🍋":
                return bet * 5
            case "🔥":
                return bet * 7
            case "🌟":
                return bet * 10
    return 0

balance = 100
bet = 0

print("*****************")
print("Slot Machine Game")
print("*****************")

while True:

    print("Symbols: 🍒 🍉 🍋 🔥 🌟")
    print("        x1.5 x3 x5 x7 x10")
    print(f"Your current balance is ${balance}")
    print()
    print()
    bet = int(input("put your bet: "))

    if bet <= 0:
        print("bet should be more than 0")
        print()
        continue
    if balance < bet:
        print("your bet should be less or equal to your balance")
        print()
        continue

    balance -= bet
    print("***************************************************")
    print()
    result = spin()
    print_row(result)
    
    amount = payout(result, bet)

    if amount == 0:
        print("sorry you didn't win")
        print()
    else:
        balance += amount
        print(f"Congratulations! You have won ${amount}")
        print()
    
    print(f"Your current balance is ${balance}")
  
    if balance == 0:
        print("***************************************************")
        print("Game over!")
        print("You lost all your Money! we are sorry for your lost")
        print("Don't Gamble Again!")
        print("***************************************************")
        break

    time.sleep(3)
    choice = input("Do you want to play again (press 0 to exit): ")

    if choice == "0":
        break

    print("***************************************************")
    print()

print()
print("***************************************************")
print("GAME OVER")
print("Thank you for gambling with us")

if balance > 100:
    print(f"You have won ${balance - 100} in gambling")

elif balance < 100:
    print(f"You have lost ${100 - balance} in gambling")

else:
    print("Your balance is still the same")

print("Don't gamble again!!!")
print("***************************************************")