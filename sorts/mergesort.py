import unittest

def mergesort(array):
    if len(array) < 2:
        return array
    middle = int(len(array)/2)
    return merge(mergesort(array[:middle]), mergesort(array[middle:]))

def merge(left, right):
    combined = []
    l = len(left)
    r = len(right)
    i = j = 0
    while i < l and j < r:
        if left[i] <= right[j]:
            combined.append(left[i])
            i += 1
        else:
            combined.append(right[j])
            j += 1
    combined += left[i:] or right[j:]
    return combined

class TestMergesort(unittest.TestCase):
    def test(self):
        self.assertEqual(mergesort([5, 5, 6, 123, 5464, 2, 0, -1]), [-1, 0, 2, 5, 5, 6, 123, 5464])
        self.assertEqual(mergesort([5, 6]), [5, 6])
        self.assertEqual(mergesort([5]), [5])
        self.assertEqual(mergesort([6, 5]), [5, 6])
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

unittest.main()
