from searching.linear_search import linear_search

import unittest


class TestLinearSearch(unittest.TestCase):
    def test(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 3)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 0), -1)
        self.assertEqual(linear_search([], 3), -1)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], None), -1)