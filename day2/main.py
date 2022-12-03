def score(strategy, score_func):
    running_score = 0
    for strat in strategy.split('\n'):
        pair = strat.split()
        running_score += score_func(pair)
    return running_score


def rock_paper_scissors_score(strategy):
    return score(strategy, native_score)


def native_score(pair):
    opp_number = ord(pair[0].upper()) - ord('A')
    player_number = ord(pair[1].upper()) - ord('X')
    if opp_number == player_number:
        return opp_number + 4
    if (player_number + 1) % 3 == opp_number:
        return player_number + 1
    return player_number + 7


def desired_score(pair):
    player_need = pair[1]
    opponent_play_ord = ord(pair[0])
    ord_a = ord('A')
    num_shape = opponent_play_ord - ord_a
    if player_need == 'Y':
        return 4 + opponent_play_ord - ord_a
    if player_need == 'X':
        return (2 + num_shape) % 3 + 1
    if player_need == 'Z':
        return (1 + num_shape) % 3 + 7


def rock_paper_scissors_desired_score(strategy):
    return score(strategy, desired_score)
