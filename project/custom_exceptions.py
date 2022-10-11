class IllegalCoordinatesExceptions(Exception):
    """ IllegalCorrdinatesExceptions should be when:
    1. try add creature at taken spot """
    def __str__(self):
        return f"Creature Probably exist on this spot"
    
class EmptyCooridinatesExceptions(Exception):
    def __str__(self):
        return f"This spot is empty"