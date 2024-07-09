
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
    left = 0
    right = len(guess) - 1
    while left < right:
        if guess[right] == "-" or guess[right] == guess[left]:
            right-=1
        if guess[left] == "0" or guess[right] == guess[left]:
            left += 1
        right-=1
    return right-1

"""
"""
#########################################################
#                   TODO                             #
#########################################################

"""
The game.py file contains an interactive game of Tic Tac Toe. A Tic tac toe game starts with a blank
cell of the game board and two players and a number of players that are marked. Each player has two lines 
of code:

a: the first game has a start:
start_game()   - prints a welcome message
draw_board()    - prints a game's board
next_turn()    - asks the team what they are trying to win. 0 for nobody, 1 for player one, and 2 for bot.

The game uses strings - a list whose index is the number used to identify the respective player.
The players pick one of the choices. Each player choose to either play against