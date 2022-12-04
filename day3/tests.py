import unittest
from day3.main import rucksack
from day3.main import common_item
from day3.main import char_score

class RuckSackTests(unittest.TestCase):
    def test_prompt_example(self):
        prompt_example = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
        self.assertEqual(rucksack(prompt_example), 157)

class commonItemTest(unittest.TestCase):
    def test_find_p(self):
        p = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(common_item(p), 'p')
        L = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        self.assertEqual(common_item(L), 'L')

    def test_char_score(self):
        self.assertEqual(char_score('p'), 16)
        self.assertEqual(char_score('L'), 38)

if __name__ == '__main__':
    unittest.main()
