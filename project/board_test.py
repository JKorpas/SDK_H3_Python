import unittest
from board import Board
from point import Point
from creature import Creature


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
        monster_from_board = self.board.get(0,2)
        self.assertEqual(self.board.map[self.point.x, self.point.y], monster_from_board)

    def test_should_return_null_when_pick_coordinates_with_no_monster(self):
        self.assertRaises(KeyError, self.board.get, 0,3)