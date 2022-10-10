import unittest
from board import Board
from point import Point
from creature import Creature
from custom_exceptions import *

class BoardTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.board = Board()
        cls.point = Point(0, 2)
        cls.creature = Creature("Centaur")
    
    def test_if_coordinates_are_0_2(self):
        self.assertEqual(self.point.get(), (0,2))

    def test_check_monster_name_if_centaur(self):
        self.assertEqual(self.creature.name, 'Centaur')
    
    def test_add_creature_to_board(self):
        self.board.add((self.point.x, self.point.y), self.creature.name)
        monster_from_board = self.board.get((0,2))
        self.assertEqual(self.board.map[self.point.x, self.point.y], monster_from_board)

    def test_should_return_null_when_pick_coordinates_with_no_monster(self):
        self.assertRaises(KeyError, self.board.get, (0,3))

    def test_cannot_add_creature_at_busy_corrdinates(self):
        self.assertRaises(IllegalCoordinatesExceptions, self.board.add, (0, 2), "Creature") 


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
        self.assertRaises(IllegalCoordinatesExceptions, self.board.move, (1,1), (0,2))

