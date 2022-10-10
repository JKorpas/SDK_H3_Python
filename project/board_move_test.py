import unittest
from board import Board
from point import Point
from creature import Creature
from custom_exceptions import *

class BoardMovingCreatureTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.point = Point(0, 2)
        self.creature = Creature("Centaur")
        self.board.add((self.point.x, self.point.y), self.creature.name)
    def test_where_monster_move_on_empty_spot(self):
        self.board.move((0,2), (0,4))
        monster_from_board = self.board.get((0,4))
        self.assertEqual(self.board.map[0, 4], monster_from_board)
        self.assertRaises(KeyError, self.board.get, (0,2))
    
    def test_where_monster_move_on_busy_spot(self):
        pass
