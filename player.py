# -*- coding: utf-8 -*-

__author__ = 'Salah Xaaji'
__copyright__ = 'Copyright 2022 Storm Hamsters'
__credits__ = 'Anja Edelmann, Ricky Raths, Lars Schneckenburger, Salah Xaaji'
__license__ = 'GPL'
__version__ = '1.0'
__created__ = '08.10.2022'
__maintainer__ = 'Salah Xaaji'
__email__ = 'xaajisal@students.zhaw.ch'
__status__ = 'Finished'


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name


if __name__ == "__main__":
    player1 = Player("Salah", "S")
    player2 = Player("Anja", "A")
    print(player1.get_name())
    print(player2.get_name())
