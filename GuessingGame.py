import random

def easyLevel():
    easyGuessToken = 6
    print("Level Easy Activated")
    target_num = random.randint(1, 10)
    while True:
        user_guess = int(input("Guess a number from 1 to 10: "))
        print(target_num)
        if user_guess == target_num:
            print("You got it right")
            break
        else:
            easyGuessToken -= 1
            print(f"That was wrong, you have {easyGuessToken} guess left")
            if easyGuessToken == 0:
                print("Game Over")
                break
        
def mediumLevel():
    easyGuessToken = 4
    print("Level Medium Activated")
    target_num = random.randint(1, 20)
    while True:
        user_guess = int(input("Guess a number from 1 to 10: "))
        print(target_num)
        if user_guess == target_num:
            print("You got it right")
            break
        else:
            easyGuessToken -= 1
            print(f"That was wrong, you have {easyGuessToken} guess left")
            if easyGuessToken == 0:
                print("Game Over")
                break

def hardLevel():
    easyGuessToken = 3
    print("Level Hard Activated")
    target_num = random.randint(1, 50)
    while True:
        user_guess = int(input("Guess a number from 1 to 10: "))
        print(target_num)
        if user_guess == target_num:
            print("You got it right")
            break
        else:
            easyGuessToken -= 1
            print(f"That was wrong, you have {easyGuessToken} guess left")
            if easyGuessToken == 0:
                print("Game Over")
                break

print("Welcome to number guessing game")
print('''
  THere are 3 level
    Select level
Enter 1 to selcet Easy
Enter 2 to selcet Medium
Enter 3 to selcet Hedium
Enter 4 to Quit
    ''')
choice = int(input("Enter a choice: "))
if choice == 1:
    easyLevel()
elif choice == 2:
    mediumLevel()
elif choice == 3:
    hardLevel()
else:
    print("Invalid input")












    
    
##    start = 1
##    ends = 10
##    guessmachine(start, ends)
##    guessnumber = ""
##    print("The guessed number is ", guessednumber)
##    while True:
##        for guessnumber in guessednumber:
##            print("You got it right")
##        
##        if guessednumber != guessnumber:
##            guessnumber = int(input("That was wrong : "))
##            easyGuessToken = easyGuessToken + 1
##        
##    #print("You got it right")
##elif choice == 2:
##    print("Level Medium Activated")
##elif choice == 3:
##    print("Level Hard Activated")
##elif choice == 4:
##    print("I hope you enjoyed the game, have a nice day")
##else:
##    print("Invalid input")

##
##
##
##target_num, guess_num = random.randint(1, 10), 0
####while target_num != guess_num:
####    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
######print('Well guessed!')
##import random
##def gg():
##    target_num, guess_num = random.randint(1, 10), 2
##    return target_num
##guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
##while gg() != guess_num:
##    guess_num = int(input('tryagin : '))
##print('Well guessed!')
