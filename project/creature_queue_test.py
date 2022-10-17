import unittest

from creature import Creature
from creature_queue import CreatureQueue
from creature_statistic import CreatureStatistic

class TestCreatureQueue(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        cls.a = Creature()
        cls.b = Creature()
        cls.c = Creature()
        cls.creature_list_test = [cls.a, cls.b, cls.c]


    def test_if_active_creature_is_correct(self):
        creature_queue = CreatureQueue(self.creature_list_test)
        self.assertEqual(self.a, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.b, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.c, creature_queue.get_active_creature())

    def test_if_queue_is_rotating(self):
        creature_queue = CreatureQueue(self.creature_list_test)
        self.assertEqual(self.a, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.b, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.c, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.a, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.b, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.c, creature_queue.get_active_creature())
        creature_queue.next()
        self.assertEqual(self.a, creature_queue.get_active_creature())