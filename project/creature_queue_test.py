import unittest
from creature import Creature
from creature_queue import CreatureQueue

class TestCreatureQueue(unittest.TestCase):
    def setUpModule(cls):
        cls.a = Creature()
        cls.b = Creature()
        cls.c = Creature()
        cls.creature_list = [cls.a,cls.b,cls.c]

    def test_if_active_creature_is_correct(self):
        creature_queue = CreatureQueue(self.creature_list)
        self.assertEqual(self.a, creature_queue.get_active_creatures())
        creature_queue.next()
        self.assertEqual(self.b, creature_queue.get_active_creatures())
        creature_queue.next()
        self.assertEqual(self.c, creature_queue.get_active_creatures())