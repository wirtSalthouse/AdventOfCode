import unittest
from day4.main import pairs_contain
from day4.main import num_of_contained_pairs
from day4.main import pairs_overlap
from day4.main import num_of_overlap_pairs


class PairsContainTestPartOne(unittest.TestCase):
    def test_pairs_contain(self):
        self.assertEqual(pairs_contain('2-8,3-7'), True)
        self.assertEqual(pairs_contain('6-6,4-6'), True)
        self.assertEqual(pairs_contain('2-3,4-5'), False)
        self.assertEqual(pairs_contain('7-47,48-67'), False)

    def test_num_of_contain_pairs(self):
        prompt_example = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
        self.assertEqual(num_of_contained_pairs(prompt_example), 2)


class PairsOverLapTest(unittest.TestCase):
    def test_pairs_overlap(self):
        self.assertEqual(pairs_overlap('5-7,7-9'), True)
        self.assertEqual(pairs_overlap('2-4,6-8'), False)
        self.assertEqual(pairs_overlap('2-8,3-7'), True)
        self.assertEqual(pairs_overlap('2-3,4-5'), False)
        self.assertEqual(pairs_overlap('45-47,11-30'), False)

    def test_num_of_pairs_overlap(self):
        prompt_example = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
        self.assertEqual(num_of_overlap_pairs(prompt_example), 4)

if __name__ == '__main__':
    unittest.main()
