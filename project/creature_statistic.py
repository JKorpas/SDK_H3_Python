class CreatureStatistic:
    def __init__(self, c_name: str, c_att: int, c_armor: int, c_max_hp: int, c_speed: int):
        self.name = c_name
        self.attack = c_att
        self.armor = c_armor
        self.max_hp = c_max_hp
        self.speed = c_speed
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("String name for creature")
        self._name = value
    
    @property
    def attack(self):
        return self._attack
    @attack.setter
    def attack(self, value):
        if not isinstance(value,int):
            raise TypeError("Enter integer value")
        if value < 0:
            raise ValueError("Give positive number")
        self._attack = value
        
    @property
    def armor(self):
        return self._armor
    @armor.setter
    def armor(self, value):
        if not isinstance(value,int):
            raise TypeError("Enter integer value")
        if value < 0:
            raise ValueError("Give positive number")
        self._armor = value

    @property
    def max_hp(self):
        return self._max_hp
    @max_hp.setter
    def max_hp(self, value):
        if not isinstance(value,int):
            raise TypeError("Enter integer value")
        if value < 0:
            raise ValueError("Give positive number")
        self._max_hp = value

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, value):
        if not isinstance(value,int):
            raise TypeError("Enter integer value")
        if value < 0:
            raise ValueError("Give positive number")
        self._speed = value
        