from day5.main import SupplyStack

def list_to_string(lst):
    return ''.join(lst)
if __name__ == '__main__':
    f = open('puzzle_input.txt', 'r')
    test_input = f.read()
    f.close()
    stax_1 = SupplyStack(test_input)
    stax_1.move_boxes_unorderd()
    print('answer to question 1:', list_to_string(stax_1.get_top_crates()))
    stax_2 = SupplyStack(test_input)
    stax_2.move_boxes_ordered()
    print('answer to question 2:', list_to_string(stax_2.get_top_crates()))
