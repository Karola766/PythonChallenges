import unittest

from task1.errors import IllegalCarError
from task1.solution.car import Car


class CarTestCase(unittest.TestCase):

    def basic_test(self, pax_count, car_mass, gear_count):
        car = Car(pax_count, car_mass, gear_count)
        self.assertEqual(car.pax_count, pax_count, f"Passenger count should be "
                                                   f"{pax_count}")
        self.assertEqual(car.car_mass, car_mass, f"Car mass should be {car_mass}")
        self.assertEqual(car.gear_count, gear_count, f"Gear count should be {gear_count}")
        mass = car_mass + 70 * pax_count
        self.assertEqual(car.total_mass, mass, "Total mass should be car_mass + "
                                               "70*pax_count")

    def test_correct(self):
        self.basic_test(5, 1500, 3)

    def test_lower_pax_bounds(self):
        with self.assertRaises(IllegalCarError):
            self.basic_test(0, 1500, 4)

    def test_upper_pax_bounds(self):
        with self.assertRaises(IllegalCarError):
            self.basic_test(7, 1500, 4)

    def test_mass_bounds(self):
        with self.assertRaises(IllegalCarError):
            self.basic_test(4, 2100, 4)


if __name__ == '__main__':
    test = CarTestCase()
    test.test_correct()
    test.test_lower_pax_bounds()
    test.test_upper_pax_bounds()
    test.test_mass_bounds()
