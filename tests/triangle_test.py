import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # ПЛОЩАДЬ

    def test_area_zero_base_height(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_positive_integers(self):
        self.assertEqual(area(5, 4), 10.0)
        self.assertEqual(area(4, 5), 10.0)
    
    def test_area_positive_floats(self):
        self.assertEqual(area(3.5, 2), 3.5)
        self.assertEqual(area(2, 3.5), 3.5)
    
    def test_area_large_numbers(self):
        self.assertEqual(area(100000, 50000), 100000 * 50000 / 2)

    def test_area_small_numbers(self):
        self.assertAlmostEqual(area(1e-10, 1e-10), 5e-21, places=31)
    
    # ПЕРИМЕТР

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(5, 0, 0), 5)
        self.assertEqual(perimeter(0, 5, 0), 5)
        self.assertEqual(perimeter(0, 0, 5), 5)
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
    
    def test_perimeter_positive_floats(self):
        self.assertEqual(perimeter(2.5, 3.5, 4), 10.0)
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(100000, 200000, 150000), 450000)

    def test_perimeter_small_numbers(self):
        self.assertAlmostEqual(perimeter(1e-10, 1e-10, 1e-10), 3e-10, places=25)

    # НЕГАТИВНЫЕ ТЕСТЫ
    
    def test_area_negative_base_height(self):
        with self.assertRaises(ValueError):
            area(-5, 4)
        with self.assertRaises(ValueError):
            area(5, -4)
        with self.assertRaises(ValueError):
            area(-5, -4)
    
    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5)

    def test_area_invalid_types(self):
        with self.assertRaises(TypeError):
            area("5", 4)
        with self.assertRaises(TypeError):
            area(5, "4")
        with self.assertRaises(TypeError):
            area("5", "4")
        with self.assertRaises(TypeError):
            area([5], 4)
        with self.assertRaises(TypeError):
            area(5, None)
        with self.assertRaises(TypeError):
            area(None, 4)
        with self.assertRaises(TypeError):
            area(True, "5")
        with self.assertRaises(TypeError):
            area(False, True)
    
    def test_perimeter_invalid_types(self):
        with self.assertRaises(TypeError):
            perimeter("3", 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, "5")
        with self.assertRaises(TypeError):
            perimeter("3", "4", "5")
        with self.assertRaises(TypeError):
            perimeter([3], 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, 4, None)
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)
        with self.assertRaises(TypeError):
            perimeter(True, 123, "5")
        with self.assertRaises(TypeError):
            perimeter(False, True, True)


if __name__ == '__main__':
    unittest.main()