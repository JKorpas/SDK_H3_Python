
class CreatureQueue:
    def __init__(self, creature_list):
        self.creatures = creature_list
        self.active_creature = None
        self.creatures_queue = []
        self.init_queue()
        self.next()
        
    def init_queue(self):
        self.creatures_queue = self.creatures.copy()

    def get_active_creature(self):
        return self.active_creature

    def next(self):
        #New Turn
        if len(self.creatures_queue) == 0:
            self.init_queue()
        self.active_creature = self.creatures_queue.pop(0)
