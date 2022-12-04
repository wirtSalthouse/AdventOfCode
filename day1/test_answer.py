from day1.main import count_calories
from day1.main import top_three_elves

if __name__ == '__main__':
    f = open('test_input.txt', 'r')
    test_input = f.read()
    f.close()
    print('count calories: elf position and total:', count_calories(test_input))
    print('total of top three elves:', top_three_elves(test_input))