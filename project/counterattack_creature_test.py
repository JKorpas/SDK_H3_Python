import unittest
from creature import Creature

class TestCounterAttack(unittest.TestCase):
    def test_creature_should_make_counterattack(self):
        attacker = Creature ("Attacker", 10, 2, 100, 5)
        defender = Creature ("Defender", 20, 2, 100, 5)
        attacker.attack(defender)
        defender.counter_attack(attacker)
        self.assertEqual(92, defender.get_current_hp())
        self.assertEqual(82, attacker.get_current_hp())