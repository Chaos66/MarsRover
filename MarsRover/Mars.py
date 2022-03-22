class Mars:

    # Mars constructor
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    # Mars.width getter
    @property
    def width(self):
        return self._width

    # Mars.width setter
    @width.setter
    def width(self, width):
        self._width = width

    # Mars.height getter
    @property
    def height(self):
        return self._height

    # Mars.height setter
    @height.setter
    def height(self, height):
        self._height = height

    # Evaluates that Mars.width and Mars.height is the same as mars(argument).height and mars(argument).y
    def __eq__(self, mars):
        return self.width == mars.width and self.height == mars.height
