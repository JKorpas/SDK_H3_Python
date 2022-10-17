from creature_statistic import CreatureStatistic


class Creature:
    def __init__(self, c_name="DefaultName", c_att=2, c_armor=1, c_max_hp=100, c_speed=3):
        self.name = c_name
        self.stats = CreatureStatistic(c_name, c_att, c_armor,  c_max_hp, c_speed)
        self.current_hp = self.stats.max_hp
        self.counter_attack_flag = False

    def attack(self, defender: object) -> int:
        attacker = self
        if self.is_alive():
            damage = Creature.calculate_damage(attacker, defender)
            defender.current_hp -= damage
            if defender.counter_attack_flag == False:
                damage_in_counterattack = Creature.calculate_damage(defender, attacker)
                attacker.current_hp -= damage_in_counterattack
                defender.counter_attack_flag = True

    @staticmethod
    def calculate_damage(attacker: object, defender: object) -> int:
        if attacker.stats.attack <= defender.stats.armor:
            damage_to_deal = 0
        else:
            damage_to_deal = attacker.stats.attack - defender.stats.armor
        return damage_to_deal

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def get_current_hp(self):
        return self.current_hp

    #Hashable object as element of dict 
    def __repr__(self) -> str:
        return f"{self.__dict__}"
    def __hash__(self):
        return hash((self.__dict__))


attacker = Creature ("Attacker", 10, 2, 100, 5)
defender = Creature ("Defender", 5, 5, 100, 5)
attacker