class IllegalCorrdinatesExceptions(Exception):
    """ IllegalCorrdinatesExceptions should be when:
    1. try add creature at taken spot """
    def __str__(self):
        return f"Creature Problalby exist on this spot"