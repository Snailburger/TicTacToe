# -*- coding: utf-8 -*-

""" Computer player """

__author__ = 'Salah Xaaji'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '08.10.2022'
__maintainer__ = 'Salah Xaaji'
__email__ = 'xaajisal@students.zhaw.ch'
__status__ = 'Finished'

import random

import player as pl


class CompPlayer(pl.Player):

    # return a random field of a list of free fields
    def choose_field(self, free_spaces):
        print(self.name)
        return random.choice(free_spaces)


if __name__ == "__main__":
    player1 = CompPlayer("Ricky", "R")
    print(player1.get_name())
