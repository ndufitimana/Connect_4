""" A static evaluator that MinMax uses to score the board
This static evaluator scores its position on the board. 
Middle positions score high because they are more valuable to winning and
side positions score less because they are less valuable to winnig.
"""
from ConnectGame import ConnectGame
from random import choice
def connectBasicEval(state):
    player1, player2 = 0, 0
    if state.isTerminal():
        if state.winner() == 1:
            return 99999
        elif state.winner() == -1:
            return -99999
        else:
            return 0
    else:
        scores1 = [   
           [4, 5, 7, 9, 7, 5, 4],
           [5, 8, 11, 15, 11, 8, 5],
           [7, 11, 17, 20, 17, 11, 7],
           [7, 11, 17, 20, 17, 11, 7],
           [5, 8, 11, 15, 11, 8, 5],
           [4, 5, 7, 9, 7, 5, 4]]

        for r in range(len(state.board)):
            for c in range(len(state.board[0])):
                if state.board[r][c] == 1:
                    player1 +=scores1[r][c]
                elif state.board[r][c] == -1:
                    player2 +=scores1[r][c]
    return player1 - player2


if __name__ == '__main__':
    """
    Create a game of Mancala.  Try 10 random moves and check that the
    heuristic is working properly. 
    """
    print("\nTESTING CONNECT  HEURISTIC")
    print("-"*50)
    game1 = ConnectGame()
    print(game1)
    for i in range(10):
        move = choice(game1.availableMoves())
        print("\nmaking move", move)
        print("\n turns", game1.turn)
        game1 = game1.makeMove(move)
        print(game1)
        score = connectBasicEval(game1)
        print("basicEval score", score)

