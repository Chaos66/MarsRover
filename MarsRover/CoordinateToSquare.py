class CoordinateToSquare:

    # CoordinateToSquare constructor
    def __init__(self, x, y, width):
        # calculation to return the grid number location of the rover
        self.square = (y - 1) * width + x

    # CoordinateToSquare getter
    @property
    def square(self):
        return self._square

    # CoordinateToSquare setter
    @square.setter
    def square(self, square):
        self._square = square
