from creature_statistic import CreatureStatistic


class Creature:
    def __init__(self, c_name="DefaultName", c_att=2, c_armor=1, c_max_hp=100, c_speed=3):
        self.name = c_name
        self.stats = CreatureStatistic(c_name, c_att, c_armor,  c_max_hp, c_speed)
        self.current_hp = self.stats.max_hp

    def attack(self, defender: object) -> int:
        defender.current_hp = defender.current_hp - (self.stats.attack - defender.stats.armor)

    def get_current_hp(self):
        return self.current_hp

    #Hashable object as element of dict 
    def __repr__(self) -> str:
        return f"{self.__dict__}"
    def __hash__(self):
        return hash((self.__dict__))
        