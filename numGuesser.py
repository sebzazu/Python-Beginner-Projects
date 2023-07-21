import random

TOTAL_GUESSES = 5
guesses = 0

def getNumber(n):
    num = random.randint(0,n)
    return num


userInput = int(input("What is the highest value you would like to use? "))

if userInput == int:
    break
num = getNumber(userInput)

while True:

    userGuess = int(input("Input your guess: "))

    

    if userGuess == num:
        print("Correct! You Win!")
        break

    else:
        guesses += 1
        print(f"Wrong! You have {TOTAL_GUESSES-guesses} left")

        if guesses == 0:
            print(f"YOU LOSE, THE NUMBER WAS {num}")
            break