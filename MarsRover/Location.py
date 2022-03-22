class Location:

    # Location constructor
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    # Location self.x getter
    @property
    def x(self):
        return self._x

    # Location self.x setter
    @x.setter
    def x(self, x):
        self._x = x

    # Location self.y getter
    @property
    def y(self):
        return self._y

    # Location self.y setter
    @y.setter
    def y(self, y):
        self._y = y

    # Evaluates that Location.x and Location.y is the same as location(argument).x and location(argument).y
    def __eq__(self, location):
        return self.x == location.x and self.y == location.y
