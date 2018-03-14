import unittest

def quicksort(array):
    inplace_quicksort(array, 0, len(array) - 1)
    return array

def inplace_quicksort(array, start, end):
    if start >= end:
        return
    if len(array) < 2:
        return
    lptr = start
    rptr = end - 1
    pivot = array[end]
    while lptr <= rptr:
        while lptr <= rptr and array[lptr] <= pivot:
            lptr += 1
        while rptr >= lptr and array[rptr] >= pivot:
            rptr -= 1
        if lptr < rptr:
            array[lptr], array[rptr] = array[rptr], array[lptr]
    array[lptr], array[end] = array[end], array[lptr]
    inplace_quicksort(array, start, lptr - 1)
    inplace_quicksort(array, lptr + 1, end)

class TestQuicksort(unittest.TestCase):
    def test(self):
        self.assertEqual(quicksort([5, 6, 123, 5464, 2, 0, -1]), [-1, 0, 2, 5, 6, 123, 5464])
        self.assertEqual(quicksort([5, 6]), [5, 6])
        self.assertEqual(quicksort([5]), [5])
        self.assertEqual(quicksort([6, 5]), [5, 6])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

unittest.main()
