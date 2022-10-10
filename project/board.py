
from creature import Creature
from point import Point
from custom_exceptions import IllegalCoordinatesExceptions

class Board():
    def __init__(self):
        self.map = dict()

    def add(self, coordinates, monster):
        if coordinates in self.map.keys():
            raise IllegalCoordinatesExceptions
        self.map[coordinates] = monster

    def get(self, coordinates):
        # print(f"{self.map[(Point(x,y))]}")
        #dupa = Point(x,y)
        return self.map[coordinates]

    def move(self, current_coordinates, new_coordinates):
        if (new_coordinates) in self.map.keys():
            raise IllegalCoordinatesExceptions
        self.map[new_coordinates] = self.map.pop(current_coordinates)
    def __eq__(self, other: object) -> bool:
        """Overrides the default implementation. Can be unnessescary"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False



if __name__ == '__main__':
    plansza = Board()
    plansza.add((0, 2), "Centaur")
    plansza.add((0, 3), "Dupa")
    plansza.move((0,2), (1,1))
    print(plansza.get((1,1)))


