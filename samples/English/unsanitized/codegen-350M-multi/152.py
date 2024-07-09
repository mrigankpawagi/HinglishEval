
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    #print game.scores,guess
    assert len(game.scores)==len(guess)
    guess_1=guess[0]
    guess_2=guess[1]
    guess_3=guess[2]
    guess_4=guess[3]
    guess_5=guess[4]
    guess_6=guess[5]
    score_1=game.scores[0]
    score_2=game.scores[1]
    score_3=game.scores[2]
    score_4=game.scores[3]
    score_5=game.scores[4]
    score_6=game.scores[5]
    difference_1=score_1+guess_2-score_3
    difference_2=score_4+guess_5-score_6
    m_game=game.clone()
    for i in range(len(game.scores)): 
        m_game.guess_moves[i]=(m_game.scores[i]==difference_1