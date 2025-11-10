import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # ПЛОЩАДЬ

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 5), 0)
    
    def test_area_positive_integers(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(10, 5), 50)
    
    def test_area_positive_floats(self):
        self.assertEqual(area(2.5, 4.0), 10.0)
        self.assertEqual(area(3.5, 2.0), 7.0)
    
    def test_area_large_numbers(self):
        self.assertEqual(area(100000, 200000), 20000000000)
    
    def test_area_small_numbers(self):
        self.assertAlmostEqual(area(1e-10, 1e-10), 1e-20, places=30)

    # ПЕРИМЕТР
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 5), 10)
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(10, 5), 30)
    
    def test_perimeter_positive_floats(self):
        self.assertEqual(perimeter(2.5, 4.0), 13.0)
        self.assertEqual(perimeter(3.5, 2.0), 11.0)
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(100000, 200000), 600000)

    def test_perimeter_very_small_numbers(self):
        self.assertAlmostEqual(perimeter(1e-10, 1e-10), 4e-10, places=25)

    # НЕГАТИВНЫЕ ТЕСТЫ
    
    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)
        with self.assertRaises(ValueError):
            area(-5, -10)

    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("5", 10)
        with self.assertRaises(TypeError):
            area(5, "10")
        with self.assertRaises(TypeError):
            area("5", "10")
        with self.assertRaises(TypeError):
            area([5], 10)
        with self.assertRaises(TypeError):
            area(5, None)
        with self.assertRaises(TypeError):
            area(None, 10)
        with self.assertRaises(TypeError):
            area(True, 10)
        with self.assertRaises(TypeError):
            area(False, True)


    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(5, -10)
        with self.assertRaises(ValueError):
            perimeter(-5, -10)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("5", 10)
        with self.assertRaises(TypeError):
            perimeter(5, "10")
        with self.assertRaises(TypeError):
            perimeter("5", "10")
        with self.assertRaises(TypeError):
            perimeter([5], 10)
        with self.assertRaises(TypeError):
            perimeter(5, None)
        with self.assertRaises(TypeError):
            perimeter(None, 10)
        with self.assertRaises(TypeError):
            perimeter(True, False)


if __name__ == '__main__':
    unittest.main()