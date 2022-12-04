from day3.main import rucksack
if __name__ == '__main__':
    f = open('puzzle_input.txt', 'r')
    test_input = f.read()
    f.close()
    print(rucksack(test_input))