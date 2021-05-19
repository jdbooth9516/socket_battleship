
from board import Board
from pieces import Ship
from player import Player
import time


class Game:

    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 1
        self.run = False
        self.winner = None

    def run_game(self):
        print("Welcome to 2 player Battleship")
        time.sleep(1)
        print()
        print("For this game you will need another human player as there is no AI")
        time.sleep(1)
        print()
        print("After your turn you will need to move so that you can not see the screen")
        time.sleep(1)
        print()
        print("When you are asked for an entry to place a ship or attack you will need to enter a number between 1 and 10.")
        print("The Columns are the numbers on the top of the board and the Rows are the numbers on the side of the board.")
        time.sleep(1)
        print()

        print("Other than that follow the on game prompts for the game play")
        time.sleep(1)
        print()


        # ADD INSTRUCTIONS ABOVE HERE
        self.run = True
        print("Player 1")
        self.player_1.set_name()
        print("Player 2 ")
        self.player_2.set_name()

        # PLAYER 1 PLACES PIECES
        self.show_board()
        self.place_piece()
        self.clear_screen()

        #PLAYER 2 PLACE PIECES
        self.show_board()
        self.place_piece()
        self.clear_screen()

        #START MAIN LOOP HERE
        self.main()

    def main(self):

        while self.run == True:
            self.show_board()
            self.attack()
            self.get_ship_destruction()
            self.get_winner()
            self.handle_turn()

    def place_piece(self):

        if self.turn == 1:
            valid_1 = False
            length = len(self.player_1.pieces)
            print(f'{self.player_1.name} please place your pieces')

            for i in range(length):

                while valid_1 == False:
                    direction = self.player_1.pieces[i].set_direction()
                    col = self.player_1.pieces[i].set_piece_colum()
                    row = self.player_1.pieces[i].set_piece_row()
                    size = self.player_1.pieces[i].size
                    space_for_ship = True

                    if col <= 0 or col > 10 or row <= 0 or row > 10:
                        print("Invalid entry: entries must be numbers between 1 and 10. Please try again")
                        space_for_ship = False
                    else:
                        for j in range(size):
                            if direction == 'vertical':
                                if self.player_1.own_board.grid[row + j][col] != ' # ':
                                    print(" Invaild enter not enough space for the ship")
                                    space_for_ship = False
                                    break
                            elif direction == 'horizontal':
                                if self.player_1.own_board.grid[row][col + j] != ' # ':
                                    print(" Invaild enter not enough space for the ship")
                                    space_for_ship = False
                                    break

                    if space_for_ship == True:
                        valid_1 = True
                        self.player_1.own_board.grid[row][col] = self.player_1.pieces[i].id

                        if direction == 'vertical':
                            for j in range(self.player_1.pieces[i].size):
                                self.player_1.own_board.grid[row + j][col] = self.player_1.pieces[i].id


                        elif direction == 'horizontal':
                            for j in range(self.player_1.pieces[i].size):
                                self.player_1.own_board.grid[row][col + j] = self.player_1.pieces[i].id
                valid_1 = False
                self.show_board()

        else:
            valid_2 = False
            length = len(self.player_2.pieces)
            print(f'{self.player_2.name} please place your pieces')

            for i in range(length):

                while valid_2 == False:
                    direction = self.player_2.pieces[i].set_direction()
                    col = self.player_2.pieces[i].set_piece_colum()
                    row = self.player_2.pieces[i].set_piece_row()
                    size = self.player_2.pieces[i].size
                    space_for_ship = True

                    if col <= 0 or col > 10 or row <= 0 or row > 10:
                        print("Invalid entry: entries must be numbers between 1 and 10. Please try again")
                        space_for_ship = False

                    else:
                        for j in range(size):
                            if direction == 'vertical':
                                if self.player_2.own_board.grid[row + j][col] != ' # ':
                                    print(" Invaild enter not enough space for the ship")
                                    space_for_ship = False
                                    break
                            elif direction == 'horizontal':
                                if self.player_2.own_board.grid[row ][col + j] != ' # ':
                                    print(" Invaild enter not enough space for the ship")
                                    space_for_ship = False
                                    break


                    if space_for_ship == True:
                        valid_2 = True
                        self.player_2.own_board.grid[row][col] = self.player_2.pieces[i].id

                        if direction == 'vertical':
                            for j in range(self.player_2.pieces[i].size):
                                self.player_2.own_board.grid[row + j][col] = self.player_2.pieces[i].id


                        elif direction == 'horizontal':
                            for j in range(self.player_2.pieces[i].size):
                                self.player_2.own_board.grid[row][col + j] = self.player_2.pieces[i].id

                valid_2 = False
                self.show_board()

        self.handle_turn()

    def show_board(self):

        if self.turn == 1:
            player_1_attack = self.player_1.attack_board.grid
            player_1_own = self.player_1.own_board.grid
            length = len(player_1_attack)
            print("Player 1 ATTACK BOARD")

            for i in range(length):
                print(player_1_attack[i])
            print("Player 1 OWN_BOARD")

            for i in range(length):
                print(player_1_own[i])

        elif self.turn == 2:
            player_2_attack = self.player_2.attack_board.grid
            player_2_own = self.player_2.own_board.grid
            length = len(player_2_attack)
            print("Player 2 ATTACK BOARD")

            for i in range(length):
                print(player_2_attack[i])
            print("Player 2 OWN_BOARD")

            for i in range(length):
                print(player_2_own[i])
        print()

    def handle_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1
        self.clear_screen()

    def attack(self):
        col = 0
        row = 0
        valid = False
        while valid == False:
            col = int(input("Choose a column to attack :"))
            row = int(input("Choose a row to attack :"))
            if col > 0 and col <= 10 and row > 0 and row <= 10:
                valid = True
            else:
                print("Invalid entry: entries must be numbers between 1 and 10. Please try again")

        if self.turn == 1:

            if self.player_2.own_board.grid[row][col] == ' # ':
                print("MISSED")
                self.player_1.attack_board.grid[row][col] = ' M '

            elif self.player_2.own_board.grid[row][col] != ' # ':
                print("HIT")
                time.sleep(2)

                if self.player_2.own_board.grid[row][col] == ' D ':
                    self.player_2.pieces[0].size -= 1
                elif self.player_2.own_board.grid[row][col] == ' S ':
                    self.player_2.pieces[1].size -= 1

                elif self.player_2.own_board.grid[row][col] == ' B ':
                    self.player_2.pieces[2].size -= 1

                elif self.player_2.own_board.grid[row][col] == ' A ':
                    self.player_2.pieces[3].size -= 1

                self.player_1.attack_board.grid[row][col] = ' H '
                self.player_2.own_board.grid[row][col] = ' H '
            self.clear_screen()

        elif self.turn == 2:

            if self.player_1.own_board.grid[row][col] == ' # ':
                print("MISSED")
                time.sleep(1)
                self.player_2.attack_board.grid[row][col] = ' M '

            elif self.player_1.own_board.grid[row][col] != ' # ':
                print("HIT")
                time.sleep(1)

                if self.player_1.own_board.grid[row][col] == ' D ':
                    self.player_1.pieces[0].size -= 1

                elif self.player_1.own_board.grid[row][col] == ' S ':
                    self.player_1.pieces[1].size -= 1

                elif self.player_1.own_board.grid[row][col] == ' B ':
                    self.player_1.pieces[2].size -= 1

                elif self.player_1.own_board.grid[row][col] == ' A ':
                    self.player_1.pieces[3].size -= 1

                self.player_2.attack_board.grid[row][col] = ' H '
                self.player_1.own_board.grid[row][col] = ' H '
            self.clear_screen()

    def get_ship_destruction(self):
        if self.turn == 1:
            length = len(self.player_2.pieces)

            for i in range(length):
                if self.player_2.pieces[i].size == 0:
                    print(f"{self.player_2.name}'s {self.player_2.pieces[i].name} is sunk")
                    time.sleep(1)
                    print()

        elif self.turn == 2:
            length = len(self.player_1.pieces)

            for i in range(length):
                if self.player_1.pieces[i].size == 0:
                    print(f"{self.player_1.name}'s {self.player_1.pieces[i].name} is sunk")
                    time.sleep(1)
                    print()

    def get_winner(self):
        if self.turn == 1:
            length = len(self.player_2.pieces)

            for i in range(length):
                if self.player_2.pieces[i].size != 0:
                    return

            print(f"{self.player_2.name}'s ships have been destroyed")
            time.sleep(2)
            print()
            print(f'{self.player_1.name} Has won the game')
            self.run = False

        elif self.turn == 2:
            length = len(self.player_1.pieces)

            for i in range(length):
                if self.player_1.pieces[i].size != 0:
                    return

            print(f"{self.player_1.name}'s ships have been destroyed")
            time.sleep(2)
            print()
            print(f'{self.player_2.name} Has won the game')
            self.run = False

    def clear_screen(self):
        for i in range(25):
            print()

