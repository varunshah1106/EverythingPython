from sorts.quicksort import quicksort
from sorts.mergesort import mergesort
import unittest


class TestQuicksort(unittest.TestCase):
    def test(self):
        self.assertEqual(quicksort([5, 6, 123, 5464, 2, 0, -1]), [-1, 0, 2, 5, 6, 123, 5464])
        self.assertEqual(quicksort([5, 6]), [5, 6])
        self.assertEqual(quicksort([5]), [5])
        self.assertEqual(quicksort([6, 5]), [5, 6])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])


class TestMergesort(unittest.TestCase):
    def test(self):
        self.assertEqual(mergesort([5, 5, 6, 123, 5464, 2, 0, -1]), [-1, 0, 2, 5, 5, 6, 123, 5464])
        self.assertEqual(mergesort([5, 6]), [5, 6])
        self.assertEqual(mergesort([5]), [5])
        self.assertEqual(mergesort([6, 5]), [5, 6])
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])


unittest.main(exit = False)
