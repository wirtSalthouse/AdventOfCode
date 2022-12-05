from day4.main import num_of_contained_pairs

if __name__ == '__main__':
    f = open('puzzle_input.txt', 'r')
    test_input = f.read()
    f.close()
    print('the answer to part 1 is', num_of_contained_pairs(test_input))