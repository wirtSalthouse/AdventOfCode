from day5.main import SupplyStack

def list_to_string(lst):
    return ''.join(lst)
if __name__ == '__main__':
    f = open('puzzle_input.txt', 'r')
    test_input = f.read()
    f.close()
    stax = SupplyStack(test_input)
    stax.move_all_boxes()
    print('answer to question 1:',list_to_string(stax.get_top_crates()))

