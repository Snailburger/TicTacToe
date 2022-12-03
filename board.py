# -*- coding: utf-8 -*-

""" Board for Game """

__author__ = 'Lars Schneckenburger'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '11.10.2022'
__maintainer__ = 'Lars Schneckenburger'
__email__ = 'schnela@students.zhaw.ch'
__status__ = 'Finished'

from colorama import Fore
from colorama import Style


class Board:

    def __init__(self, rows, columns):
        self.rows = rows  # number of rows
        self.columns = columns  # number of columns
        self.init_value = 0  # value for free space on board
        self.board = list()
        self.winner_combo = list()

    def make_new_board(self):
        """
        Makes a new Board.
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.

        """
        self.board = [[self.init_value for column_n in range(self.columns)]
                      for row_n in range(self.rows)]

    def get_free_spaces(self):
        """
        Parameters
        ----------
        None.

        Returns
        -------
        List with available spaces

        """
        free_spaces = list()
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.board[i][j] == self.init_value):
                    free_spaces.append((i, j))
        return free_spaces

    def show_board(self):
        """
        Print board to console.
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.

        """
        # with this variable it can be defined, how the empty board looks like
        empty_field = ' '

        # Header row
        print(f"  ", end='')
        for j in range(self.rows):
            print(f"| {j + 1} ", end='')
        print("| ")
        print((self.columns * 4 + 4) * "-")

        # Other rows
        for i in range(self.rows):
            print(f"{i + 1} ", end='')
            for j in range(self.columns):
                # check if Field is empty
                if self.board[i][j] == self.init_value:
                    print(f"| {empty_field} ", end='')
                elif (i, j) in self.winner_combo:
                    # prints the winner coordinate red
                    print(f"| {Fore.RED}{self.board[i][j]} {Style.RESET_ALL}", end='')
                else:
                    # prints either sign of player 1 or player 2
                    print(f"| {self.board[i][j]} ", end='')
            print("| ")
            print((self.columns * 4 + 4) * "-")

    # sets a field with the postion and symbol
    def set_field(self, position: tuple, symbol: str):
        self.board[position[0]][position[1]] = symbol


if __name__ == "__main__":

    try:
        board_1 = Board(3, 3)
        board_1.make_new_board()
        print(board_1.board)
        board_1.show_board()
        board_1.set_field((0, 0), "X")
        board_1.show_board()
        a = board_1.get_free_spaces()
        print(a)


    except Exception as Error:
        print(Error)

    print("\ndone")
    print("Author: {}".format(__author__))
    print("Credits: {}".format(__credits__))
