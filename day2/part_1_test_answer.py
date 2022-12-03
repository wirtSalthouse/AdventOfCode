from day2.main import rock_paper_scissors_score

if __name__ == '__main__':
    f = open('problem_set.txt', 'r')
    test_input = f.read()
    f.close()
    print(rock_paper_scissors_score(test_input))