from board import Board
from pieces import *

class Player:
    def __init__(self):
        self.name = ""
        self.attack_board = Board()
        self.own_board = Board()
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.battleship = Battleship()
        self.aircraft = Aircraft_carrier()

        self.pieces = [self.destroyer, self.submarine, self.battleship, self.aircraft]

    def set_name(self):
        name = input("Please enter a name: ")
        self.name = name