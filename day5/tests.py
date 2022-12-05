import unittest

from day5.main import SupplyStack


class SettersAndGetters(unittest.TestCase):
    def test_stack_representation(self):
        f = open('test_input_1.txt', 'r')
        nput = f.read()
        f.close()
        stax = SupplyStack(nput)
        # todo: assert representations of both private members

    def test_stack_string(self):
        f = open('test_input_1.txt', 'r')
        nput = f.read()
        f.close()
        stack_string_0 = '[Z] [M] [P]\n 1   2   3'
        model_0 = [['Z'], ['M'], ['P']]
        stax = SupplyStack(nput)
        self.assertEqual(stax.parse_stack(stack_string_0), model_0)
        stack_string_1 =  '    [D]\n[N] [C]\n[Z] [M] [P]\n 1   2   3'
        model_1 = [['Z', 'N'], ['M', 'C', 'D'], ['P']] #note starting from base up, since the heights are variable
        self.assertEqual(stax.parse_stack(stack_string_1), model_1)
        stack_string_2 = '        [Z]\n        [N]\n[M]     [D]\n[C]     [P]\n1   2   3'
        model_2 = [['C', 'M'], [], ['P', 'D', 'N', 'Z']]
        self.assertEqual(stax.parse_stack(stack_string_2), model_2)

    def test_instructions(self):
        f = open('test_input_1.txt', 'r')
        nput = f.read()
        f.close()
        stax = SupplyStack(nput)
        stax.set_stack([['Z', 'N'], ['M', 'C', 'D'], ['P']])
        stax.move_boxes('move 1 from 2 to 1')
        answer_1 = [['Z', 'N', 'D'], ['M', 'C'], ['P']]
        self.assertEqual(stax.get_stack(), answer_1)
        stax.move_boxes('move 3 from 1 to 3')
        answer_2 = [[], ['M', 'C'], ['P', 'D', 'N', 'Z']]
        self.assertEqual(stax.get_stack(), answer_2)

    def test_top_crates(self):
        f = open('test_input_1.txt', 'r')
        nput = f.read()
        f.close()
        stax = SupplyStack(nput)
        stax.set_stack([['Z', 'N'], ['M', 'C', 'D'], ['P']])
        top_crates = ['N', 'D', 'P']
        self.assertEqual(stax.get_top_crates(), top_crates)
        stax.set_stack([['C', 'M'], [], ['P', 'D', 'N', 'Z']])
        top_crates_2 = ['M', '', 'Z']
        self.assertEqual(stax.get_top_crates(), top_crates_2)


if __name__ == '__main__':
    unittest.main()
