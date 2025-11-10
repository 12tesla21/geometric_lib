import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from src.square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # ПЛОЩАДЬ

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)
    
    def test_area_positive_integer(self):
        self.assertEqual(area(5), 25)
    
    def test_area_positive_float(self):
        self.assertEqual(area(3.5), 12.25)
    
    def test_area_large_number(self):
        self.assertEqual(area(1000000), 1000000000000)

    def test_area_small_numbers(self):
        self.assertAlmostEqual(area(1e-10), 1e-20, places=30)

    # ПЕРИМЕТР
    
    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive_integer(self):
        self.assertEqual(perimeter(5), 20)
    
    def test_perimeter_positive_float(self):
        self.assertEqual(perimeter(3.5), 14.0)
    
    def test_perimeter_large_number(self):
        self.assertEqual(perimeter(100000000), 4 * 100000000)

    def test_perimeter_small_numbers(self):
        self.assertAlmostEqual(perimeter(1e-10), 4e-10, places=25)

    # НЕГАТИВНЫЕ ТЕСТЫ

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-5)
    
    def test_perimeter_negative_side(self):
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
            area({"side": 5})
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
            perimeter({"side": 5})
        with self.assertRaises(TypeError):
            perimeter(True)
        with self.assertRaises(TypeError):
            perimeter(False)


if __name__ == '__main__':
    unittest.main()