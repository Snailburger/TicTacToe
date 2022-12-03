# -*- coding: utf-8 -*-

""" Game functionality """

__author__ = 'Salah Xaaji, Ricky Raths'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '08.10.2022'
__maintainer__ = 'Salah Xaaji'
__email__ = 'xaajisal@students.zhaw.ch'
__status__ = 'Finished'

import random
import string

import numpy as np

from board import Board
from compplayer import CompPlayer
from humanplayer import HumanPlayer


class Game:

    def __init__(self):
        self.board = Board(3, 3)
        self.running = False
        self.players = list()  # a list of the players playing a game
        self.choosing_player_type = True
        self.choosing_player_symbol = True

    def start(self):
        """
        Clears the board and sets parameter self.running = True
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.

        """
        self.board.make_new_board()
        self.running = True

    def show_menu(self):
        """
        Menu options after the first round

        Parameters
        ----------
        None.

        Returns
        -------
        None.

        """

        print("Menu options: Press one of the following keys")
        print("R: Rematch")
        print("N: New Match with new players")
        print("Q: Quit")

    def run_game(self, new_players, automatic=False):
        """
        Runs a classic round of Tic Tac Toe
        
        Parameters
        ----------
        new_players: True or False. If True, new players can be created.
        automatic: True or False. True if game is run manually. False if game is run automatically.

        Returns
        -------
        Returns the value of check_winner()

        """

        round_count = 0
        print()
        print("Welcome to TicTacToe!\n")

        if new_players:
            self.players = list()
            self.choose_players()

        self.start()

        while self.running:
            self.board.winner_combo = list()

            # returns 0 or 1 as index number for the list self.players
            active_player = self.players[round_count % 2]

            self.board.show_board()

            player_choice = self.player_choice(active_player)

            self.board.set_field(player_choice, active_player.symbol)

            win = self.check_winner()
            if win == 0:  # no winner
                round_count = round_count + 1
                continue
            elif win == 1:  # it's a draw
                print("It's a draw... ")

            else:  # there is a winner
                print("The winner is:", active_player.get_name())

            self.board.show_board()

            if not automatic:
                choosing_menu = True
                while choosing_menu:  # runs as long as no valid input has been made
                    self.show_menu()
                    menu_option = input("What would you like to do?")
                    if menu_option.upper() not in ["R", "N", "Q"]:
                        print("Not a valid option. Please try again.")
                    else:
                        if menu_option.upper() == "R":
                            choosing_menu = False
                            self.run_game(new_players=False)
                        elif menu_option.upper() == "N":
                            choosing_menu = False
                            self.run_game(new_players=True)
                        elif menu_option.upper() == "Q":
                            choosing_menu = False
                            self.end()
            else:
                self.end()
        return win

    def verify_move(self, move):
        """
        Validates the move of the player.
        
        Parameters
        ----------
        move: tuple (coordinates of the board)

        Returns
        -------
        True: if move is valid
        False: if move is invalid

        """
        valid_moves = self.board.get_free_spaces()
        if move in valid_moves:
            return True
        else:
            return False

    def check_winner(self):
        """
        Check if there is a winner.
        If there is a winner the symbol of the winner is returned.
        
        Parameters
        ----------
        None.

        Returns
        -------
        1: for a draw and
        0: no winner at the moment

        """
        n = 0
        for row in self.board.board:
            if len(set(row)) == 1 and str(row[0]) != "0":
                self.board.winner_combo = [(n, 0), (n, 1), (n, 2)]
                return row[0]
            else:
                n += 1
        n = 0
        for column in np.transpose(self.board.board):
            if len(set(column)) == 1 and str(column[0]) != "0":
                self.board.winner_combo = [(0, n), (1, n), (2, n)]
                return column[0]
            else:
                n += 1
        n = 0
        for diagonal in [[row[i] for i, row in enumerate(self.board.board)],
                         [row[-i - 1] for i, row in enumerate(self.board.board)]]:
            if len(set(diagonal)) == 1 and str(diagonal[0]) != "0":
                if n == 0:
                    self.board.winner_combo = [(0, 0), (1, 1), (2, 2)]
                else:
                    self.board.winner_combo = [(2, 0), (1, 1), (0, 2)]
                return diagonal[0]
            else:
                n += 1

        if len(self.board.get_free_spaces()) < 1:
            return 1

        return 0

    # Choose the players
    def choose_players(self):
        """
        Define players. Add different players to self.players.
        
        Parameters
        ----------
        None.

        Returns
        -------
        None.

        """
        print("*Choose Players*")

        characters = list(string.ascii_letters[26:52])  # list with alphabet

        for i in range(2):

            self.choosing_player_type = True
            # self.choosing will be False once a valid player has been created

            while self.choosing_player_type:
                print("\nPlayer ", i + 1)
                try:
                    type_of_player = int(input("Human Player or Computer? \n"
                                               "Choose 0 for computer or 1 for a human player [0/1]"))
                except Exception:
                    print("Invalid input. Please use integer 0 or 1.")
                    continue

                if type_of_player == 1:
                    player_name = str(input("What's the name of the player?"))

                    # cycle to validate the chosen symbol
                    self.choosing_player_symbol = True
                    while self.choosing_player_symbol:
                        player_symbol = str(input("Symbol Player? (Choose a single character)"))
                        if (len(player_symbol) == 1 and not player_symbol == "0"
                                and not player_symbol == "1"):
                            self.players.append(HumanPlayer(player_name, player_symbol))
                            self.choosing_player_symbol = False
                            self.choosing_player_type = False
                            if player_symbol.upper() in characters:
                                characters.remove(player_symbol.upper())
                        else:
                            print("Invalid input. Please try again.")

                elif type_of_player == 0:
                    computer_symbol = random.choice(characters)
                    self.players.append(CompPlayer("Computer", computer_symbol))
                    self.choosing_player_type = False
                    characters.remove(computer_symbol)

                else:
                    print("Invalid input. Please try again.")

    # Choice player
    def player_choice(self, active_player):
        """
        Player chooses an empty field
        
        Parameters
        ----------
        active_player: which player is next

        Returns
        -------
        player_choice: coordinates of move

        """
        if isinstance(active_player, CompPlayer):
            player_choice = active_player.choose_field(self.board.get_free_spaces())
            return player_choice
        else:
            # Turns False as soon as the player made a valid move
            while True:
                player_choice = active_player.choose_field()
                if player_choice != -1 and self.verify_move(player_choice):
                    return player_choice
                else:
                    print("Invalid Move. Please Try again.")
                    self.board.show_board()

    def end(self):
        self.running = False


if __name__ == "__main__":
    tictactoe = Game()
    tictactoe.run_game(True)
