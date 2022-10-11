

class Creature:
    def __init__(self, name="None"):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise TypeError("String name for creature")
        self._name = value

    def __repr__(self) -> str:
        return f"{self.name}"
    def __hash__(self):
        return hash((self.name))