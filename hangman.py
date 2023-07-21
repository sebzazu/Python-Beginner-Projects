import random
from words import words

def getWord(words):
        word = random.choice(words)

        while ' ' in word or '-' in word:
             word = random.choice(words)

        return word.upper()

def playGame(word):
    blankList = []
    wrongGuesses = 0
    over = False

    for i in range(len(word)):
            blankList.append('_') 
    while over == False:
        playerInput = input("Guess a letter or the word ").upper()

        if playerInput == word:
            print("Correct! You win!")
            over = True
        else:
            rightGuess = False
            for i, letter in enumerate(word):
                if playerInput == letter:
                    rightGuess = True
                    blankList[i] = letter
                   
        
            if rightGuess == False:
                wrongGuesses +=1
            
                if wrongGuesses == 1:
                    print('0')
                if wrongGuesses == 2:
                    print('0\n'
                        '|')
                if wrongGuesses == 3:
                    print(' 0\n'
                        '/|')
                if wrongGuesses == 4:
                    print(' 0\n'
                        '/|\\')
                if wrongGuesses == 5:
                    print(' 0\n'
                        '/|\\\n'
                        ' /')
                if wrongGuesses == 6:
                    print(' 0\n'
                        '/|\\\n'
                        ' /\\')
                
                    print("You Lost! The Word was: " + word)
                    break    
        print(blankList)


while True:
    activeWord = getWord(words)
    playGame(activeWord)

    playAgain = input("Do you want to play again? (y/n)")

    if playAgain == 'y':
        continue
    if playAgain == 'n':
        break

