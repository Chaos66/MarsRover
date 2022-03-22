import unittest
from MarsRover.Pilot import Pilot


class TestPilot(unittest.TestCase):
    # Test Pilot constructor with argument
    def test_pilot_constructor_input(self):
        pilot_name = Pilot("Oz")
        self.assertEqual(pilot_name.pilot_name, "Oz")

    # Test Pilot constructor with no argument
    def test_pilot_constructor_no_input(self):
        pilot_name = Pilot()
        self.assertEqual(pilot_name.pilot_name, "Unknown Pilot")

    # Test Pilot setter and getter
    def test_pilot_setter(self):
        pilot_name = Pilot()
        pilot_name.pilot_name = "Oz"
        self.assertEqual(pilot_name.pilot_name, "Oz")


if __name__ == '__main__':
    unittest.main()
