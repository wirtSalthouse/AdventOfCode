from day2.main import rock_paper_scissors_score
from day2.main import rock_paper_scissors_desired_score

if __name__ == '__main__':
    f = open('problem_set.txt', 'r')
    test_input = f.read()
    f.close()
    print("total score in case 1:%d" %(rock_paper_scissors_score(test_input)))
    print("total score in case 2:%d" % (rock_paper_scissors_desired_score(test_input)))