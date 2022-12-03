# -*- coding: utf-8 -*-

""" Calculate outcome probabilities """

__author__ = 'Ricky Raths'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '08.10.2022'
__maintainer__ = 'Ricky Raths'
__email__ = 'rathsric@students.zhaw.ch'
__status__ = 'Finished'

import os

from compplayer import CompPlayer
from game import Game

if __name__ == "__main__":
    tictactoe = Game()
    lars = CompPlayer("Lars", "L")
    anja = CompPlayer("Anja", "A")

    number_of_games = 1000
    wins = 0
    losses = 0
    draws = 0

    tictactoe.players = [lars, anja]

    for i in range(0, number_of_games):
        result = tictactoe.run_game(False, True)
        if result == tictactoe.players[0].symbol:
            wins = wins + 1
        elif result == tictactoe.players[1].symbol:
            losses = losses + 1
        else:
            draws = draws + 1

    wins_p = 100 / float(number_of_games) * wins
    losses_p = 100 / float(number_of_games) * losses
    draws_p = 100 / float(number_of_games) * draws

    os.system("cls")

    print("Statistics of Player:", lars.get_name())
    print("W:", wins, "L:", losses, "D:", draws)
    print("Wins:", wins_p, "%")
    print("Losses:", losses_p, "%")
    print("Draws:", draws_p, "%")

    print("GOAL: Wins: 51.4")
    print("GOAL: Losses: 30.5")
    print("GOAL: Draws: 18.1")
