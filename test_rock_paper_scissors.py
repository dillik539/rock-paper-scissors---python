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

        # etc....


    def test_get_choice(self):
        #TODO write this test 
        pass


if __name__ == '__main__':
    unittest.main()
