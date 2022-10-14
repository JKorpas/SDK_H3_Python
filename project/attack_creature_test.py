import unittest
from creature import Creature

class TestAttackCreature(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.attacker = Creature ("Attacker", 10, 2, 100, 5)
        cls.defender = Creature ("Defender", 5, 5, 100, 5)
        
    def test_creature_should_lost_5hp_when_attacker_has_10_atk_and_defender_has_5_arm(self):
        self.attacker.attack(self.defender)
        self.assertEqual(95, self.defender.get_current_hp())
        