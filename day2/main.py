# This is a sample Python script.
def score_match(score_arr, player_play):
    if player_play == 'X':
        return score_arr[0]
    if player_play == 'Y':
        return score_arr[1]
    return score_arr[2]

def rock_paper_scissors_score(strategy):
    score = 0
    for strat in strategy.split('\n'):
        pair = strat.split()
        opponent_strategy = pair[0].upper()
        player_strategy = pair[1].upper()
        if opponent_strategy == 'A':
            payoffs = [4, 8, 3]
        elif opponent_strategy == 'B':
            payoffs = [1, 5, 9]
        else:
            payoffs = [7, 2, 6]
        score += score_match(payoffs, player_strategy)
    return score
