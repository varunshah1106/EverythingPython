from data_structures.min_heap import MinHeap

import unittest
import sys


class TestMinHeap(unittest.TestCase):

    def test_initiation(self):
        heap = MinHeap()
        self.assertEqual(heap.size, 0)
        self.assertEqual(heap.heapList, [])

    def test_heapify(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        self.assertEqual(heap.heapList[0], 1)

    def test_heapify_empty_array(self):
        heap = MinHeap()
        array = []
        heap.heapify(array)
        self.assertEqual(heap.heapList, [])

    def test_heapify_invalid_array(self):
        heap = MinHeap()
        array = 'invalid array'
        with self.assertRaises(TypeError) as error:
            heap.heapify(array)

    def test_minimum(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        self.assertEqual(heap.minimum(), 1)

    def test_minimum_empty_list(self):
        heap = MinHeap()
        array = []
        heap.heapify(array)
        self.assertEqual(heap.minimum(), None)

    def test_minimum_same_array(self):
        heap = MinHeap()
        array = [5, 5, 5, 5, 5]
        heap.heapify(array)
        self.assertEqual(heap.minimum(), 5)

    def test_insert(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        self.assertEqual(heap.insert(-2), True)
        self.assertEqual(heap.insert(None), False)
        self.assertEqual(heap.heapList[0], -2)

    def test_remove(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        heap.remove(index=0)
        self.assertEqual(heap.minimum(), 2)
        with self.assertRaises(IndexError) as error:
            heap.remove(11)

    def test_remove_invalid_index(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        with self.assertRaises(IndexError) as error:
            heap.remove(11)

    def test_remove_invalid_index(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        with self.assertRaises(IndexError) as error:
            heap.remove('11')

    def test_delete_min(self):
        heap = MinHeap()
        array = [5, 4, 1, 6, 9, 7, 2, 8, 3]
        heap.heapify(array)
        heap.deleteMin()
        self.assertEqual(heap.minimum(), 2)

    def test_delete_min_empty_list(self):
        heap = MinHeap()
        array = []
        heap.heapify(array)
        with self.assertRaises(IndexError) as error:
            heap.deleteMin()
