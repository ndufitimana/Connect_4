"""
The following implementatin of Connect-4 Game was inspired by an implementation
by AskPython which is part of JournalDev IT Services Private Limited. 
We improved on their implementation to use numpy and Object Oriented Programming.

The origanal Implementation can be found here: https://www.askpython.com/python/examples/connect-four-game 
"""

import numpy as np
from BoardGame import _base_game

RED = u"\033[1;31m"
BLUE = u"\033[1;34m"
RESET = u"\033[0;0m"
SQUARE = u"\u2588"

RED_BORDER = RED + "-" + RESET
BLUE_BORDER = BLUE + "|" + RESET


class ConnectGame(_base_game):
    """ 
    This class initializes the the Connect-4 game
    """
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.turn = 1
        self.board = np.zeros([self.rows, self.cols], int)

        self._moves = None
        self._terminal = None
        self._winner = None
        self._repr = None
        self._hash = None

    def __repr__(self):
        
        top = '     0 1 2 3 4 5 6 '
        side = ["f", "e", "d", "c", "b", "a"]
        if self._repr is None:
            board = np.flip(self.board.copy(), 0)
            self._repr = u"\n" + "    " + ( " " + RED_BORDER) * (self.cols) + "\n"
            for i in range(self.rows):
                self._repr += " " + side[i] + " " + BLUE_BORDER + " "
                for j in range(self.cols):
                    self._repr += self._print_char(board[i, j]) + " "
                self._repr += BLUE_BORDER + "\n"
            self._repr += "    " + (" " + RED_BORDER) * self.cols + "\n" + top
        return self._repr

    def makeMove(self, move):
        """
        This functino returns a new Connect-4 game where  a move has been made
        """
        cg = ConnectGame()
        row = self.get_next_open_row(move)
        cg.board = np.array(self.board)
        cg.board[row, move] = self.turn
        cg.turn = -self.turn
        return cg

    def availableMoves(self):
        """ 
        returns the availables valid moves that a player can make
        """
        if self._moves is None:
            self._moves = []
            for i in range(len(self.board[self.rows-1])):
               if self.board[self.rows-1][i] == 0:
                   self._moves.append(i)
        return self._moves

    def get_next_open_row(self, col):
        """
        A helper function that returns the next available row in a given column
        """
        for r in range(self.rows):
            if self.board[r][col] == 0:
                return r


    def winning_move(self, S):
        """
        A helper function that checks whether the current state has a win or not
        for any of the players.
        The function goes through the board vertically, horizontaly and diagonally 
        """
        game = False   
        # Horizontal checker
        for j in range(0,6):
            for i in range(3,7):
                if (self.board[j, i]==self.board[j, i-1]==\
                    self.board[j, i-2]==self.board[j, i-3]==S):
                        game = True
                else:
                    continue   
        # Vertical checker
        for i in range(0,7):
            for j in range(3,6):
                if (self.board[j, i]==self.board[j-1, i]==\
                    self.board[j-2, i]==self.board[j-3, i]==S):
                        game = True
                else:
                    continue
        # Diagonal checker
        for i in range(0,4):
            for j in range(0,3):
                if (self.board[j, i]==self.board[j+1, i+1]==\
                    self.board[j+2, i+2]==self.board[j+3, i+3]==S or
                    self.board[j+3, i]==self.board[j+2, i+1]==\
                    self.board[j+1, i+2]==self.board[j, i+3]==S):
                        game = True
                else:
                    continue
        return game
    def winner(self):
        """
        Returns the winner if there is a winner when a termial state is reached 
        if there is no winner, returns 0 to indicate a draw 
        """
        if self.isTerminal():
            #if self._winner is None:
            if self.winning_move(-1) or self.winning_move(1) :
                self._winner = -1*(self.turn)
                return self._winner
        return 0

    def isTerminal(self):
        """
        Checks whether a given state is termainal. 
        A state is terminal when there is a winner or when there no other valid moves 
        that can be made.
        """
        if self._terminal is not None:
            return self._terminal
        if (self.winning_move(1) or self.winning_move(-1)) or not (0 in self.board):
            self._terminal = True
        else:
            self._terminal = False
        return self._terminal

       
