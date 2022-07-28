import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 1

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess number: "))
    if(userGuess==randNumber):
        print("Computer Number: ",randNumber)
        print("You guessed it right!")
        print("The number of guesses you take to win is :",guesses)
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
    guesses += 1

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broke the high score!")
    with open("hiscore.txt",'w') as f:
        f.write(str(guesses-1))