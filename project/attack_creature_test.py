import unittest
from creature import Creature

class TestAttackCreature(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Setting up {cls.__name__}")
        
    def test_creature_should_lost_5hp_when_attacker_has_10_atk_and_defender_has_5_arm(self):
                            #c_name, c_att, c_armor, c_max_hp, c_speed):
        attacker = Creature ("Attacker", 10, 2, 100, 5)
        defender = Creature ("Defender", 5, 5, 100, 5)
        attacker.attack(defender)
        self.assertEqual(95, defender.get_current_hp())
    
    def test_creature_should_not_heal_herself(self):
        attacker = Creature ("Attacker", 5, 2, 100, 5)
        defender = Creature ("Defender", 5, 10, 100, 5)
        attacker.attack(defender)
        self.assertEqual(100, defender.get_current_hp())