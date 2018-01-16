import random
def main():
    playAgain = "y"
    while playAgain == "y":
        randomNumber = random.randint(1,3)
        compGuess = getChoice(randomNumber)

        userGuess = getUserInput()
        getResult(compGuess,userGuess)

        playAgain = input("Do you want to play again? Enter y for yes: ")
        playAgain = playAgain.lower()
        if(playAgain!="y"):
            print("Thank you for playing. Come again.")
def getChoice(number):
    if number == 1:
        choice = "Rock"
    elif number == 2:
        choice = "Paper"
    else:
        choice = "Scissors"
    return choice

def getResult(computerGuess, userGuess):
    if computerGuess == userGuess:
        print("It's a tie. Play again.")
        print("You chose " + userGuess + ".")
        print("The computer also chose " + computerGuess + ".")
    elif ((computerGuess == "Rock" and userGuess == "Scissors") or
    (computerGuess == "Paper" and userGuess == "Rock") or
    (computerGuess == "Scissors" and userGuess == "Paper")):
        print("Oops! The computer wins.")
        print("You chose " + userGuess + ".")
        print("The computer chose " + computerGuess + ".")
    else:
        print("Congratulations! You win.")
        print("You chose " + userGuess + ".")
        print("The computer chose " + computerGuess + ".")

def getUserInput():
    user = input("Enter your choice: ")
    user = user.strip()

    first_letter = user[0].upper()
    rem_letters = user[1:].lower()
    user = first_letter + rem_letters
    return user
main()
