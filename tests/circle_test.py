import unittest
import math
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from src.circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    # ПЛОЩАДЬ

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
    
    def test_area_positive_integer(self):
        self.assertAlmostEqual(area(5), 78.53981633974483, places=7)
    
    def test_area_positive_float(self):
        self.assertAlmostEqual(area(2.5), 19.634954084936208, places=7)
    
    def test_area_large_number(self):
        self.assertAlmostEqual(area(100), 31415.926535897932, places=7)

    def test_area_small_numbers(self):
        self.assertAlmostEqual(area(1e-10), math.pi * 1e-20, places=30)
    
    # ПЕРИМЕТР
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive_integer(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793, places=7)
    
    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(2.5), 15.707963267948966, places=7)
    
    def test_perimeter_large_number(self):
        self.assertAlmostEqual(perimeter(100000), 628318.5307179587, places=7)
    
    def test_perimeter_small_numbers(self):
        self.assertAlmostEqual(perimeter(1e-10), 2 * math.pi * 1e-10, places=30)

    # НЕГАТИВНЫЕ ТЕСТЫ

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-5)
    
    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
    
    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area([5])
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            area({"radius": 5})
        with self.assertRaises(TypeError):
            area(True)
        with self.assertRaises(TypeError):
            area(False)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("5")
        with self.assertRaises(TypeError):
            perimeter([5])
        with self.assertRaises(TypeError):
            perimeter(None)
        with self.assertRaises(TypeError):
            perimeter({"radius": 5})
        with self.assertRaises(TypeError):
            perimeter(True)
        with self.assertRaises(TypeError):
            perimeter(False)


if __name__ == '__main__':
    unittest.main()