# -*- coding: utf-8 -*-

""" Tic Tac Toe"""

__author__ = 'Lars Schneckenburger'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '15.10.2022'
__maintainer__ = 'Lars Schneckenburger'
__email__ = 'schnela@students.zhaw.ch'
__status__ = 'Finished'

from game import Game

tictactoe = Game()
tictactoe.run_game(True)

print("\n" + "-" * 80)
print("Author: {}".format(__author__))
print(__copyright__)
print("Credits: {}".format(__credits__))
print("License: {}".format(__license__))
print("Version: {}".format(__version__))
print("Created: {}".format(__created__))
print("Maintainer: {}".format(__maintainer__))
print("Email: {}".format(__email__))
print("Status: {}".format(__status__))
