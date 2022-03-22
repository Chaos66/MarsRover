import unittest
from MarsRover.Location import Location
from MarsRover.Mars import Mars
from MarsRover.Rover import Rover


class TestLocation(unittest.TestCase):
    # Test the the constructor for Location with no arguments
    def test_location_constructor_no_value(self):
        test_location_1 = Location()
        self.assertEqual(test_location_1.x, 1)
        self.assertEqual(test_location_1.y, 1)

    # Test the the constructor for Location with arguments x = 55, y = 80
    def test_location_constructor_with_value(self):
        test_location_2 = Location(55, 80)
        self.assertEqual(test_location_2.x, 55)
        self.assertEqual(test_location_2.y, 80)

    # Test the setters and getters for the Location constructor
    def test_location_constructor_setter(self):
        test_location_3 = Location()
        self.assertEqual(test_location_3.x, 1)
        self.assertEqual(test_location_3.y, 1)
        test_location_3.x = 4
        test_location_3.y = 6
        self.assertEqual(test_location_3.x, 4)
        self.assertEqual(test_location_3.y, 6)

    # Test the evaluation method
    def test_evaluation(self):
        test_mars_4 = Mars(20, 20)
        test_location_4 = Location(20, 20)
        test_rover_4 = Rover(test_mars_4, test_location_4)
        self.assertEqual(test_rover_4.location, test_location_4)


if __name__ == '__main__':
    unittest.main()
