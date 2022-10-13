
class CreatureQueue:
    def __init__(self, creature_list):
        self.active_creature = None
        self.creatures_queue = creature_list.copy()
        self.next()

    def get_active_creature(self):
        return self.active_creature

    def next(self):
        self.active_creature = self.creatures_queue.pop(0)
