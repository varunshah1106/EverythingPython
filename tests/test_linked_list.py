from __future__ import print_function
from data_structures.linked_list import LinkedList

import unittest


class TestLinkedList(unittest.TestCase):
    def test_initiation(self):
        linked_list = LinkedList()
        self.assertEqual(len(linked_list), 0)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.insert(data='sample data', index=0)
        self.assertEqual(len(linked_list), 1)
        self.assertNotEqual(linked_list.head, None)
        self.assertNotEqual(linked_list.tail, None)
        linked_list = LinkedList()
        linked_list.insert(data=0, index=0)
        linked_list.insert(data=1, index=1)
        linked_list.insert(data=2, index=2)
        linked_list.insert(data=3, index=3)
        self.assertEqual(linked_list.length(), 4)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 3)
        self.assertEqual(linked_list.head.next.data, 1)
        self.assertEqual(linked_list.tail.previous.data, 2)
        self.assertEqual(linked_list.head.next.next.data, 2)
        self.assertEqual(linked_list.tail.previous.previous.data, 1)
        self.assertEqual(linked_list.head.next.next.next.data, 3)
        self.assertEqual(linked_list.tail.previous.previous.previous.data, 0)

    def test_insert_non_empty_list_index_valid_repeating(self):
        linked_list = LinkedList()
        linked_list.insert(data='sample data', index=0)
        linked_list.insert(data='new sample data', index=0)
        self.assertEqual(len(linked_list), 2)
        self.assertNotEqual(linked_list.head, None)
        self.assertNotEqual(linked_list.tail, None)

    def test_insert_non_empty_list_index_valid_non_repeating(self):
        linked_list = LinkedList()
        linked_list.insert(data='sample data', index=0)
        self.assertEqual(len(linked_list), 1)
        linked_list.insert(data='new sample data', index=1)
        self.assertEqual(len(linked_list), 2)
        linked_list.insert(data='new sample data - 2', index=1)
        self.assertEqual(len(linked_list), 3)
        self.assertNotEqual(linked_list.head, None)
        self.assertNotEqual(linked_list.tail, None)

    def test_insert_empty_list_index_invalid(self):
        linked_list = LinkedList()
        with self.assertRaises(IndexError) as error:
            linked_list.insert(data='sample data', index=1)
            self.assertEqual(len(linked_list), 0)
            self.assertEqual(linked_list.head, None)
            self.assertEqual(linked_list.tail, None)

    def test_length_zero(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.length(), 0)

    def test_length_non_zero(self):
        linked_list = LinkedList()
        linked_list.insert(data='sample data', index=0)
        self.assertEqual(linked_list.length(), 1)

    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 1)
        self.assertNotEqual(linked_list.head, None)
        self.assertNotEqual(linked_list.tail, None)

    def test_append_fail(self):
        linked_list = LinkedList()
        linked_list.append(data=None)
        self.assertNotEqual(linked_list.head, None)

    def test_node_at(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        self.assertEqual(linked_list.length(), 5)
        self.assertEqual(linked_list.nodeAt(index=2).data, 2)
        self.assertEqual(linked_list.nodeAt(index=0).data, 0)
        self.assertEqual(linked_list.nodeAt(index=4).data, 4)

    def test_node_at_index_invalid(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.nodeAt(index=-1), None)
            self.assertEqual(linked_list.nodeAt(index=4), None)

    def test_find(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=None)
        self.assertEqual(linked_list.find(1), linked_list.head.next)
        self.assertEqual(linked_list.find(None), linked_list.tail)
        self.assertEqual(linked_list.find(3), linked_list.tail.previous)
        self.assertEqual(linked_list.find(9), -1)

    def test_index_of(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=None)
        self.assertEqual(linked_list.indexOf(1), 1)
        self.assertEqual(linked_list.indexOf(None), 4)
        self.assertEqual(linked_list.indexOf(3), 3)
        self.assertEqual(linked_list.indexOf(9), -1)

    def test_value_at(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=None)
        self.assertEqual(linked_list.valueAt(1), 1)
        self.assertEqual(linked_list.valueAt(0), 0)
        self.assertEqual(linked_list.valueAt(3), 3)
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.valueAt(9), -1)

    def test_remove_at(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=None)
        self.assertEqual(linked_list.removeAt(1), True)
        self.assertEqual(linked_list.valueAt(1), 2)
        self.assertEqual(linked_list.removeAt(0), True)
        self.assertEqual(linked_list.valueAt(0), 2)
        self.assertEqual(linked_list.removeAt(1), True)
        self.assertEqual(linked_list.valueAt(1), None)
        self.assertEqual(linked_list.removeAt(1), True)
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.removeAt(1), True)

    def test_remove(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.remove(0), False)
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=None)
        self.assertEqual(linked_list.length(), 5)
        self.assertEqual(linked_list.remove(0), True)
        self.assertEqual(linked_list.valueAt(0), 1)
        self.assertEqual(linked_list.length(), 4)
        self.assertEqual(linked_list.remove(None), True)
        self.assertEqual(linked_list.length(), 3)
        self.assertEqual(linked_list.remove(0), False)
        self.assertEqual(linked_list.length(), 3)
