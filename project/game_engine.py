from board import Board
from creature import Creature
from point import Point
from creature_queue import CreatureQueue
from project.board import BOARD_WIDTH


class GameEngine:
    def __init__(self, player_1_creatures, player_2_creatures):
        self.board = Board()
        self.put_creatures_to_board(player_1_creatures, player_2_creatures)
        self.two_sides_creatures = []
        self.two_sides_creatures.extend(player_1_creatures)
        self.two_sides_creatures.extend(player_2_creatures)
        self.queue = CreatureQueue()
    
    def put_creatures_to_board(self, player_1_creatures, player_2_creatures):
        self.put_creature_at_one_side(player_1_creatures, 0)
        self.put_creature_at_one_side(player_2_creatures, BOARD_WIDTH-1)
    
    def put_creature_at_one_side(self, creatures, x_axis):
        for i, creature in enumerate(creatures):
            self.board.add((x_axis, i+1), creature)
            
    def move(self, target_point):
        self.board.move(self.queue.get_active_creature(), target_point)