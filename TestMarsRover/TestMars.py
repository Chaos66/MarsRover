import unittest

from MarsRover.Mars import Mars


class TestMars(unittest.TestCase):
    # Test to see if creating Mars object without arguments returns width and height of 0
    def test_mars_constructor_no_value(self):
        test_mars_1 = Mars()
        self.assertEqual(test_mars_1.width, 0)
        self.assertEqual(test_mars_1.height, 0)

    # Test to see if creating Mars object with argument of 7 by 7
    def test_mars_constructor_with_value_1(self):
        test_mars_2 = Mars(7, 7)
        self.assertEqual(test_mars_2.width, 7)
        self.assertEqual(test_mars_2.height, 7)

    # Test to see if creating Mars object with argument of 100 by 100
    def test_mars_constructor_with_value_2(self):
        test_mars_3 = Mars(100, 100)
        self.assertEqual(test_mars_3.width, 100)
        self.assertEqual(test_mars_3.height, 100)

    # Test the Mars setters and getters
    def test_mars_constructor_setter(self):
        test_mars_4 = Mars()
        self.assertEqual(test_mars_4.width, 0)
        self.assertEqual(test_mars_4.height, 0)
        test_mars_4.width = 11
        test_mars_4.height = 7
        self.assertEqual(test_mars_4.width, 11)
        self.assertEqual(test_mars_4.height, 7)


if __name__ == '__main__':
    unittest.main()
