# -*- coding: utf-8 -*-

""" Human player """

__author__ = 'Salah Xaaji'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '08.10.2022'
__maintainer__ = 'Salah Xaaji'
__email__ = 'xaajisal@students.zhaw.ch'
__status__ = 'Finished'

import player as pl


class HumanPlayer(pl.Player):

    # choose field with input from human
    def choose_field(self):
        try:
            print(f"{self.name}'s turn")
            user_input = tuple(input("Which field do you want?"))
            user_choice = tuple(int(coordinate) - 1 for coordinate in user_input)
            if len(user_choice) != 2:
                raise Exception
        except Exception:
            print("Oops!  That was no valid number.  Try again...")
            return -1

        return user_choice


if __name__ == "__main__":
    player1 = HumanPlayer("Ricky", "R")
    print(player1.get_name())
    a = player1.choose_field()
    print(a)
