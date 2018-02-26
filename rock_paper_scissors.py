import random
def main():
    #initialize the loop control
    playAgain = "y"
    while (playAgain == "y"):
        #generate a random number between 1 and 3.
        randomNumber = random.randint(1,3)
        #call the getChoice function.
        compGuess = getChoice(randomNumber)

        userGuess = getUserInput()

        result = getResult(compGuess,userGuess)

        output = formatWinner(result, compGuess, userGuess)
        print(output)

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

    # Figure out who won

    if computerGuess == userGuess:
        return 'Tie'

    elif ((computerGuess == "Rock" and userGuess == "Scissors") or
    (computerGuess == "Paper" and userGuess == "Rock") or
    (computerGuess == "Scissors" and userGuess == "Paper")):
        return 'Computer'

    else:
        return 'User'


def formatWinner(winner, computerGuess, userGuess):

    # Use game results to display user-friendly message

    if winner == 'Tie':
        output = "It's a tie. Play again.\nYou chose " + userGuess + ".\nThe computer also chose " + computerGuess + "."
        return output

    if winner == 'Computer':
        output = "Oops! The computer wins.\nYou chose " + userGuess + ".\nThe computer chose " + computerGuess + "."
        return output

    else:
        output = "Congratulations! You win.\nYou chose " + userGuess + ".\nThe computer chose " + computerGuess + "."
        return output


def getUserInput():

    # Suggestion: tell user what they need to enter
    # User should enter 1 = rock, 2 = paper or 3 = scissors
    # Add some validation
    # Then you can use getChoice to turn the number into "rock" or "paper" or "scissors"

    user = input("Enter your choice: ")
    user = user.strip()

    first_letter = user[0].upper()
    rem_letters = user[1:].lower()
    user = first_letter + rem_letters
    return user



if __name__ == '__main__':
    main()
