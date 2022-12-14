import unittest
from creature import Creature

class TestCounterAttack(unittest.TestCase):
    def test_creature_should_make_counterattack(self):
        attacker = Creature ("Attacker", 10, 2, 100, 5)
        defender = Creature ("Defender", 20, 5, 100, 5)
        attacker.attack(defender)
        self.assertEqual(95, defender.get_current_hp())
        self.assertEqual(82, attacker.get_current_hp())
        
    def test_creature_should_not_make_second_counterattack(self):
        attacker1 = Creature ("Attacker", 10, 2, 100, 5)
        attacker2 = Creature ("Attacker", 10, 2, 100, 5)
        defender = Creature ("Defender", 20, 5, 100, 5)
        attacker1.attack(defender)
        attacker2.attack(defender)
        self.assertEqual(90, defender.get_current_hp())
        self.assertEqual(82, attacker1.get_current_hp())
        self.assertEqual(100, attacker2.get_current_hp())