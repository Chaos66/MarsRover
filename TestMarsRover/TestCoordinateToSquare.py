import unittest

from MarsRover.CoordinateToSquare import CoordinateToSquare


class TestCoordinateToSquare(unittest.TestCase):
    # checks that the translation of example in brief spec returns correct
    def test_coordinate_to_square_constructor(self):
        location = CoordinateToSquare(24, 47, 100)
        self.assertEqual(location.square, 4624)

    # checks that the first square (1, 1) (start location of rover) returns 1
    def test_coordinate_to_square_min(self):
        location = CoordinateToSquare(1, 1, 100)
        self.assertEqual(location.square, 1)

    # checks that the last square (100, 100) of grid returns 10000
    def test_coordinate_to_square_max(self):
        location = CoordinateToSquare(100, 100, 100)
        self.assertEqual(location.square, 10000)

    # checks that the bottom left most location on grid (1, 100) returns 9901
    def test_coordinate_to_square_bottom_left(self):
        location = CoordinateToSquare(1, 100, 100)
        self.assertEqual(location.square, 9901)

    # checks that the top right most location on grid (100, 1) returns 100
    def test_coordinate_to_square_top_right(self):
        location = CoordinateToSquare(100, 1, 100)
        self.assertEqual(location.square, 100)

    # checks the result if the width of the grid is more than 100
    def test_coordinate_to_square_150_width(self):
        location = CoordinateToSquare(133, 7, 150)
        self.assertEqual(location.square, 1033)

    # checks the result if the width of the grid is less than 100
    def test_coordinate_to_square_25_width(self):
        location = CoordinateToSquare(17, 11, 25)
        self.assertEqual(location.square, 267)

    # checks the result if the width of the grid is less than 100 and not a multiple of 100
    def test_coordinate_to_square_17_width(self):
        location = CoordinateToSquare(9, 7, 17)
        self.assertEqual(location.square, 111)


if __name__ == '__main__':
    unittest.main()
