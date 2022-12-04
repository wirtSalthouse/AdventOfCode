from day3.main import rucksack
from day3.main import badge_score

if __name__ == '__main__':
    f = open('puzzle_input.txt', 'r')
    test_input = f.read()
    f.close()
    print('the answer to part 1 is', rucksack(test_input))
    print('the answer to part 2 is', badge_score(test_input) )