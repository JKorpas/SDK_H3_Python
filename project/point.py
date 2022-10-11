BOARD_WIDTH = 20
BOARD_HEIGHT = 15


class Point:
    def __init__(self, x_cor=0, y_cor=0):
        self.x_axis = x_cor
        self.y_axis = y_cor

    @property
    def x_axis(self):
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value_x):
        if not isinstance(value_x, int):
            raise TypeError("Bad type of x-cor")
        if (value_x < 0) or (value_x > BOARD_WIDTH):
            raise ValueError("X-cor should be between 0 and 20")
        self._x_axis = value_x

    @property
    def y_axis(self):
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value_y):
        if not isinstance(value_y, int):
            raise TypeError("Bad type of y-cor")
        if (value_y < 0) or (value_y > BOARD_HEIGHT):
            raise ValueError("y-cor should be between 0 and 15")
        self._y_axis = value_y
    #Easier to read func
    def __repr__(self) -> str:
        return f"{self._x_axis, self.y_axis}"
    #Allow object of this class to be part of dict
    def __hash__(self):
        return hash((self.get()))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self._x_axis == other._x_axis and self._y_axis == other._y_axis
        return NotImplemented

    # Wrapper to make test easier to read
    def get(self):
        return (self._x_axis, self._y_axis)
