import unittest
from day2.main import rock_paper_scissors_score

class RockPaperScissorsScores(unittest.TestCase):

    def test_rock_beats_scissors(self):
        strategy = 'A Z'
        # score is 3 (scissors) + 0
        self.assertEqual(rock_paper_scissors_score(strategy), 3)

    def test_rock_loses_to_paper(self):
        strategy = 'A Y'
        # score is 2 (paper) + 6
        self.assertEqual(rock_paper_scissors_score(strategy), 8)

    def test_rock_rock_rock_tie(self):
        strategy = 'A X'
        # score is 2 (paper) + 6
        self.assertEqual(rock_paper_scissors_score(strategy), 4)

    def test_paper_loses_to_scissors(self):
        #strategy = [['B', 'Z']]
        strategy = 'B Z'
        # score is 3 (scissors) + 6
        self.assertEqual(rock_paper_scissors_score(strategy), 9)

    def test_paper_beats_rock(self):
        strategy = 'B X'
        # score is 1 (rock) + 0
        self.assertEqual(rock_paper_scissors_score(strategy), 1)

    def test_paper_paper_tie(self):
        strategy = 'B Y'
        # score is 2 (paper) + 3
        self.assertEqual(rock_paper_scissors_score(strategy), 5)

    def test_scissors_loses_to_rock(self):
        strategy = 'C X'
        # score is 1 (rock) + 6
        self.assertEqual(rock_paper_scissors_score(strategy), 7)

    def test_scissors_beats_paper(self):
        strategy = 'C Y'
        # score is 2 (paper) + 0
        self.assertEqual(rock_paper_scissors_score(strategy), 2)

    def test_scissors_scissors_tie(self):
        strategy = 'C Z'
        # score is 3 (scissors) + 3
        self.assertEqual(rock_paper_scissors_score(strategy), 6)

    def test_prompt_example(self):
        strategy = 'A Y\nB X\nC Z'
        self.assertEqual(rock_paper_scissors_score(strategy), 15)

    def test_prompt_example_case_insentive(self):
        strategy = 'a Y\nB x\nC Z'
        self.assertEqual(rock_paper_scissors_score(strategy), 15)

if __name__ == '__main__':
    unittest.main()
