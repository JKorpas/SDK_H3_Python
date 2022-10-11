BOARD_WIDTH = 20
BOARD_HEIGHT = 15


class Point:
    def __init__(self, x_axis, y_axis):
        self._x_axis = x_axis
        self._y_axis = y_axis

    @property
    def x_axis(self):
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if not isinstance(value, int):
            raise TypeError("Bad type of x-cor")
        if 0 <= value <= BOARD_WIDTH:
            raise ValueError("X-cor should be between 0 and 20")
        self._x_axis = value

    @property
    def y_axis(self):
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if not isinstance(value, int):
            raise TypeError("Bad type of y-cor")
        if 0 <= value <= BOARD_HEIGHT:
            raise ValueError("y-cor should be between 0 and 15")
        self._y_axis = value

    def __repr__(self) -> str:
        return f"X: {self._x_axis} Y: {self._y_axis}"

    def __hash__(self):
        return hash((self.get()))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return self._x_axis == other._x_axis and self._y_axis == other._y_axis
        return NotImplemented

    #Wrapper to make test easier to read
    def get(self):
        return (self._x_axis, self._y_axis)
