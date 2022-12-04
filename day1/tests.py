import unittest
from day1.main import count_calories
from day1.main import top_three_elves

class ElfLines(unittest.TestCase):
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

class TopThreeElves(unittest.TestCase):

    def test_only_one_elf(self):
        one_elf_one_load = '3000'
        self.assertEqual(top_three_elves(one_elf_one_load), 3000)
        one_elf_many_loads = "1000\n2000\n3000"
        self.assertEqual(top_three_elves(one_elf_many_loads), 6000)

    def test_two_elves(self):
        two_elves_one_load = '3000\n\n3000'
        self.assertEqual(top_three_elves(two_elves_one_load), 6000)
        two_elves_many_loads = '1000\n2000\n3000\n\n4000'
        self.assertEqual(top_three_elves(two_elves_many_loads), 10000)

    def test_three_elves(self):
        three_elves_1 = '1000\n2000\n3000\n\n4000\n\n5000'
        self.assertEqual(top_three_elves(three_elves_1), 15000)
        three_elves_2 = '9000\n\n10000\n\n7000\n8000\n9000'
        self.assertEqual(top_three_elves(three_elves_2), 43000)

    def test_top_three_elves(self):
        complicated_elves = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n\n7000\n8000\n9000"
        self.assertEqual(top_three_elves(complicated_elves), 59000)
        complicated_elves_2 = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n\n7000\n8000\n8000"
        self.assertEqual(top_three_elves(complicated_elves_2), 58000)


if __name__ == '__main__':
    unittest.main()
