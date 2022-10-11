from typing import Type
from custom_exceptions import IllegalCoordinatesExceptions,EmptyCooridinatesExceptions
from point import Point
from creature import Creature
BOARD_WIDTH = 20
BOARD_HEIGHT = 15


class Board():
    def __init__(self):
        self.map = dict()
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT

    def add(self, coordinates: Point, monster="None"):
        self.throw_IllegalCoordinatesExceptions(coordinates)
        self.map[coordinates] = monster

    def get(self, coordinates: Point):
        self.throw_EmptyCooridinatesExceptions(coordinates)
        return self.map[coordinates]

    def move(self, current_coordinates: Point, new_coordinates: Point):
        self.throw_IllegalCoordinatesExceptions(new_coordinates)
        self.map[new_coordinates] = self.map.pop(current_coordinates)



    def throw_IllegalCoordinatesExceptions(self, coordinates: Point):
        if coordinates in self.map.keys():
            raise IllegalCoordinatesExceptions

    def throw_EmptyCooridinatesExceptions(self, coordinates: Point):
        if coordinates not in self.map.keys():
            raise EmptyCooridinatesExceptions


if __name__ == '__main__':
    plansza = Board()
    stwor = Creature("Pikinier")
    punkt = Point(1,2)
    plansza.add(Point(20,15), Creature("Pikinier"))
    print(plansza.map)



"""        if 0 <= coordinates._x <= BOARD_WIDTH:
            raise ValueError("X-cor should be between 0 and 20")
        if 0 <= coordinates._y <= BOARD_HEIGHT:
            raise ValueError("y-cor should be between 0 and 15")
        if not isinstance(coordinates._x, int) and isinstance(coordinates._y, int):
            raise TypeError("Bad type of coordinatess")"""
