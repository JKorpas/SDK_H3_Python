
from creature import Creature
from point import Point


class Board():
    def __init__(self):
        self.map = dict()

    def add(self, coordinates, monster):
        self.map[coordinates] = monster

    def get(self, x, y):
        # print(f"{self.map[(Point(x,y))]}")
        #dupa = Point(x,y)
        return self.map[x, y]

    def __eq__(self, other: object) -> bool:
        """Overrides the default implementation. Can be unnessescary"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == '__main__':
    plansza = Board()
    plansza.add((0, 2), "Centaur")
    plansza.add((0, 3), "Dupa")
    plansza.add((0, 3), "asdas")
    #plansza.get(0,4)
    print(plansza.get(0,3))


