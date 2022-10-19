import unittest
from creature import Creature
from creature_queue import CreatureQueue


class TestCounterAttackFlag(unittest.TestCase):
    def test_creature_counterattack_flag_should_reset_in_new_turn(self):
        attacker1 = Creature ("Attacker", 10, 2, 100, 6)
        attacker2 = Creature ("Attacker", 10, 2, 100, 5)
        defender = Creature ("Defender", 20, 5, 100, 4)
        creature_list_test = [attacker1, attacker2, defender]
        creature_queue = CreatureQueue(creature_list_test)
        attacker1.attack(defender)
        attacker2.attack(defender)
        #1st turn
        self.assertEqual(90, defender.get_current_hp())
        self.assertEqual(82, attacker1.get_current_hp())
        self.assertEqual(100, attacker2.get_current_hp())
        #2nd turn
        creature_queue.init_queue()
        attacker1.attack(defender)
        attacker2.attack(defender)
        self.assertEqual(80, defender.get_current_hp())
        self.assertEqual(64, attacker1.get_current_hp())
        self.assertEqual(100, attacker2.get_current_hp())