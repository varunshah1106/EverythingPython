from searching.linear_search import linear_search
from searching.binary_search import binary_search
from searching.interpolation_search import interpolation_search
from searching.jump_search import jump_search

import unittest


class TestLinearSearch(unittest.TestCase):
    def test(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4, 5, -23, -34, 0], 3), 2)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(linear_search([], 3), -1)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], None), -1)


class TestBinarySearch(unittest.TestCase):
    def test(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], None), -1)


class TestInterpolationSearch(unittest.TestCase):
    def test(self):
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(interpolation_search([], 3), -1)
        self.assertEqual(interpolation_search([1, 2, 3, 4, 5], None), -1)


class TestJumpSearch(unittest.TestCase):
    def test(self):
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(jump_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(jump_search([], 3), -1)
        self.assertEqual(jump_search([1, 2, 3, 4, 5], None), -1)
