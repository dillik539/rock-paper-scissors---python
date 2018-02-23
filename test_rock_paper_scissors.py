import rock_paper_scissors
import unittest

class TestRockPaperScissors(unittest.TestCase):
    def test_get_result(self):
        compGuess = "Rock"
        userGuess = "Rock"
        expected = "It's a tie. Play again.\nYou chose " + userGuess + ".\nThe computer also chose " + compGuess + "."
        self.assertEqual(expected, rock_paper_scissors.getResult(compGuess,userGuess))

        compGuess = "Paper"
        userGuess = "Rock"
        expected = "Oops! The computer wins.\nYou chose " + userGuess + ".\nThe computer chose " + compGuess + "."
        self.assertEqual(expected, rock_paper_scissors.getResult(compGuess, userGuess))

        compGuess = "Rock"
        userGuess = "Paper"
        expected = "Congratulations! You win.\nYou chose " + userGuess + ".\nThe computer chose " + compGuess + "."
        self.assertEqual(expected, rock_paper_scissors.getResult(compGuess, userGuess))



if __name__ == '__main__':
    unittest.main()
