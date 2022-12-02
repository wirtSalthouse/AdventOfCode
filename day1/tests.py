import unittest
from day1.main import count_calories

class oneElfLines(unittest.TestCase):
    def test_one_elf_one_load_line(self):
        one_elf_line_1 = "5000"
        self.assertEqual(count_calories(one_elf_line_1), (1, 5000))
        one_elf_line_2 = "2000"
        self.assertEqual(count_calories(one_elf_line_2), (1, 2000))

    def test_one_elf_multiple_load_line(self):
        one_elf_line_1 ="5000\n2000"
        self.assertEqual(count_calories(one_elf_line_1), (1, 7000))
        one_elf_line_2 = "2000\n2000"
        self.assertEqual(count_calories(one_elf_line_2), (1, 4000))

    def test_two_elf_one_load_lines(self):
        two_elf_line_1 = "5000\n\n4000"
        self.assertEqual(count_calories(two_elf_line_1), (1, 5000))
        two_elf_line_2 = "6000\n\n9000"
        self.assertEqual(count_calories(two_elf_line_2), (2, 9000))

    def test_multi_elves_multi_loads(self):
        prompt_example = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        self.assertEqual(count_calories(prompt_example), (4, 24000))
        different_example = "20000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"
        self.assertEqual(count_calories(different_example), (1, 25000))

    def test_err_cases(self):
        self.assertEqual(count_calories(''), False)
        words = "6000\n\n9000\n30000\nmeat\n6000"
        self.assertEqual(count_calories(words), False)

    def test_tie_cases(self):
        elves = "2000\n\n2000"
        self.assertEqual(count_calories(elves), (1, 2000))
        complicated_elves = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n\n7000\n8000\n9000"
        self.assertEqual(count_calories(complicated_elves), (4, 24000))

if __name__ == '__main__':
    unittest.main()
