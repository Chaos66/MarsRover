class Rover:
    # BEARING dictionary
    BEARING = {
        'N': 1,
        'E': 2,
        'S': 3,
        'W': 4,
    }

    # Rover constructor
    def __init__(self, mars, location, bearing):
        self.mars = mars
        self.location = location
        self.bearing = bearing

    # Rover.bearing getter
    @property
    def bearing(self):
        return self._bearing

    # Rover.bearing setter
    @bearing.setter
    def bearing(self, bearing):
        if bearing < 1:
            self._bearing = 4
        elif bearing > 4:
            self._bearing = 1
        else:
            self._bearing = bearing

    # Rover.move function
    def move(self, move):
        if self.BEARING['N'] == self._bearing:
            if self.location.y - move >= 1:
                self.location.y -= move
            else:
                raise Exception("This is outside of the allowed area")
        elif self.BEARING['E'] == self._bearing:
            if self.location.x + move <= self.mars.width:
                self.location.x += move
            else:
                raise Exception("This is outside of the allowed area")
        elif self.BEARING['S'] == self._bearing:
            if self.location.y + move <= self.mars.height:
                self.location.y += move
            else:
                raise Exception("This is outside of the allowed area")
        elif self.BEARING['W'] == self._bearing:
            if self.location.x - move >= 1:
                self.location.x -= move
            else:
                raise Exception("This is outside of the allowed area")

    # Rover.turn_left method
    def turn_left(self):
        self.bearing = self._bearing - 1

    # Rover.turn_right method
    def turn_right(self):
        self.bearing = self._bearing + 1
