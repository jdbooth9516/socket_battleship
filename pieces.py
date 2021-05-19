class Ship:
    def __init__(self):
        self.name = ''
        self.size = 0
        self.direction = ' '

    def set_direction(self):
        direction = input("pick a direction to place the ship: type 'h' for horizontal or 'v' for vertical: ")
        if direction == 'h':
            self.direction = 'horizontal'
            return self.direction
        else:
            self.direction = 'vertical'
            return self.direction

    def set_piece_colum(self):

        column_cord = int(input(f'select column cordinate to place your {self.name}: '))
        return column_cord

    def set_piece_row(self):
        row_cord = int(input(f'select row cordinate to place your {self.name}: '))
        return row_cord


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = ' Destroyer '
        self.id = ' D '
        self.size = 2


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = ' Submarine '
        self.id = ' S '
        self.size = 3


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = ' Battleship '
        self.id = ' B '
        self.size = 4


class Aircraft_carrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = ' Aircraft_carrier '
        self.id = ' A '
        self.size = 5