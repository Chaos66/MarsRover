import unittest

from MarsRover.Mars import Mars
from MarsRover.Location import Location
from MarsRover.Rover import Rover


class TestRover(unittest.TestCase):
    # Test the rover constructor
    def test_rover_constructor(self):
        mars = Mars(20, 20)
        location = Location()
        rover_1 = Rover(mars, location, Rover.BEARING['S'])
        self.assertEqual(rover_1.location, location)
        self.assertEqual(rover_1.mars, Mars(20, 20))
        self.assertEqual(rover_1.bearing, 3)
        self.assertEqual(rover_1.location.x, 1)
        self.assertEqual(rover_1.location.y, 1)

    # Test the rover setter and getters
    def test_rover_x_and_y_getter_and_setter(self):
        mars = Mars(20, 20)
        location = Location(20, 20)
        rover_2 = Rover(mars, location, Rover.BEARING['W'])
        rover_2.location.x = 11
        rover_2.location.y = 15
        rover_2.bearing = rover_2.bearing - 1
        self.assertEqual(rover_2.bearing, 3)
        self.assertEqual(rover_2.location, location)

    # Test rover move function
    def test_rover_move(self):
        mars = Mars(20, 20)
        location = Location(10, 10)
        rover_3 = Rover(mars, location, Rover.BEARING['N'])
        rover_3.move(5)
        self.assertEqual(rover_3.location.y, 5)

        location = Location(10, 10)
        rover_3 = Rover(mars, location, Rover.BEARING['S'])
        rover_3.move(5)
        self.assertEqual(rover_3.location.y, 15)

        location = Location(10, 10)
        rover_3 = Rover(mars, location, Rover.BEARING['E'])
        rover_3.move(5)
        self.assertEqual(rover_3.location.x, 15)

        location = Location(10, 10)
        rover_3 = Rover(mars, location, Rover.BEARING['W'])
        rover_3.move(5)
        self.assertEqual(rover_3.location.x, 5)

    # Test rover turn_left and turn_right function
    def test_rover_turn(self):
        mars = Mars(20, 20)
        location = Location(10, 10)
        rover_3 = Rover(mars, location, Rover.BEARING['N'])
        self.assertEqual(rover_3.bearing, 1)
        rover_3.turn_left()
        self.assertEqual(rover_3.bearing, 4)
        rover_3.turn_right()
        self.assertEqual(rover_3.bearing, 1)
        rover_3.turn_right()
        self.assertEqual(rover_3.bearing, 2)


if __name__ == '__main__':
    unittest.main()
