import unittest
from project.creature import Creature
from project.creature_queue import CreatureQueue


class TestCreatureQueue(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.a = Creature("A")
        cls.b = Creature("B")
        cls.c = Creature("C")
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