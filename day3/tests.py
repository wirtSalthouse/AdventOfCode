import unittest
from day3.main import rucksack
from day3.main import common_item
from day3.main import char_score
from day3.main import find_badge
from day3.main import badge_score


class part1Tests(unittest.TestCase):
    def test_prompt_example(self):
        prompt_example = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
        self.assertEqual(rucksack(prompt_example), 157)

    def test_find_p(self):
        p = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(common_item(p), 'p')
        L = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        self.assertEqual(common_item(L), 'L')

    def test_char_score(self):
        self.assertEqual(char_score('p'), 16)
        self.assertEqual(char_score('L'), 38)


class part2Fests(unittest.TestCase):

    def test_we_dont_need_no_stinking_badges(self):
        sack_arr_1 = ['vJrwpWtwJgWrhcsFMMfFFhFp',
                    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                    'PmmdzqPrVvPwwTWBwg']
        self.assertEqual(find_badge(sack_arr_1), 'r')
        sack_arr_2 = [
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw',
        ]
        self.assertEqual(find_badge(sack_arr_2), 'Z')

    def test_badge_scores(self):
        prompt_example = "vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg" \
                         "\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw "
        self.assertEqual(badge_score(prompt_example), 70)

    def multiple_of_three_safeguard(self):
        bad_input = "baloneyentrythatthrowsoffthecount\nvJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL" \
                    "\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw "
        self.assertEqual(badge_score(bad_input), False)

if __name__ == '__main__':
    unittest.main()
