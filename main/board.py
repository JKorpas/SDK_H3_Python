from point import Point
from creature import Creature


class Board:
    def __init__(self, coordinates: Point, monster: Creature):
        self.board = dict()
        self.board[coordinates] = monster
        
