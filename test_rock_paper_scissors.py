from rock_paper_scissors import formatWinner, getResult, getChoice

import unittest

class TestRockPaperScissors(unittest.TestCase):

    def test_output(self):
        compGuess = "Rock"
        userGuess = "Rock"
        expected = "It's a tie. Play again.\nYou chose " + userGuess + ".\nThe computer also chose " + compGuess + "."
        self.assertEqual(expected, formatWinner("Tie", compGuess,userGuess))

        compGuess = "Paper"
        userGuess = "Rock"
        expected = "Oops! The computer wins.\nYou chose " + userGuess + ".\nThe computer chose " + compGuess + "."
        self.assertEqual(expected, formatWinner("Computer", compGuess, userGuess))

        compGuess = "Rock"
        userGuess = "Paper"
        expected = "Congratulations! You win.\nYou chose " + userGuess + ".\nThe computer chose " + compGuess + "."
        self.assertEqual(expected, formatWinner("User", compGuess, userGuess))



    def test_result(self):
        self.assertEqual("Tie", getResult("Rock", "Rock"))
        self.assertEqual("Computer", getResult("Rock", "Scissors"))
        self.assertEqual("Computer", getResult("Paper", "Rock"))
        self.assertEqual("Computer", getResult("Scissors", "Paper"))
        self.assertEqual("User", getResult("Paper", "Scissors"))
        self.assertEqual("User", getResult("Scissors", "Rock"))
        self.assertEqual("User", getResult("Rock", "Paper"))


    def test_get_choice(self):
        self.assertEqual("Rock", getChoice(1))
        self.assertEqual("Paper", getChoice(2))
        self.assertEqual("Scissors", getChoice(3))


if __name__ == '__main__':
    unittest.main()
