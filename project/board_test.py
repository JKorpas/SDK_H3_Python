import unittest

from board import Board
from point import Point
from creature import Creature
from custom_exceptions import IllegalCoordinatesExceptions, EmptyCooridinatesExceptions


class BoardTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.board = Board()
        cls.point = Point(0, 2)
        cls.creature = Creature("Centaur")

    def test_if_coordinates_are_0_2(self):
        self.assertEqual(self.point.get(), (0, 2))

    def test_check_monster_name_if_centaur(self):
        self.assertEqual(self.creature.name, 'Centaur')

    def test_add_creature_to_board(self):
        self.board.add((self.point._x_axis, self.point._y_axis),
                       self.creature.name)
        monster_from_board = self.board.get((0, 2))
        self.assertEqual(
            self.board.map[self.point._x_axis, self.point._y_axis], monster_from_board)

    def test_should_return_keyerror_when_pick_coordinates_with_no_monster(self):
        self.assertRaises(EmptyCooridinatesExceptions, self.board.get, (0, 3))

    def test_cannot_add_creature_at_busy_corrdinates(self):
        self.assertRaises(IllegalCoordinatesExceptions,
                          self.board.add, (0, 2), "Creature")
