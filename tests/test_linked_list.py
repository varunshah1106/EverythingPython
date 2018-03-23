from __future__ import print_function
from data_structures.linked_list import LinkedList
from mock import patch
from io import StringIO

import unittest
import sys


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

    def test_find_unsuccessful(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        self.assertEqual(linked_list.find(9), -1)

    def test_find_empty_list(self):
        linked_list = LinkedList()
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

    def test_index_of_unsuccessful(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        self.assertEqual(linked_list.indexOf(9), -1)

    def test_index_of_empty_list(self):
        linked_list = LinkedList()
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

    def test_value_at_unsuccessful(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.valueAt(9), -1)

    def test_value_at_empty_list(self):
        linked_list = LinkedList()
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

    def test_remove_at_unsuccessful(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.removeAt(5), False)

    def test_remove_at_empty_list(self):
        linked_list = LinkedList()
        with self.assertRaises(IndexError) as error:
            self.assertEqual(linked_list.removeAt(1), True)

    def test_remove(self):
        linked_list = LinkedList()
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

    def test_remove_unsuccessful(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        self.assertEqual(linked_list.remove(5), False)

    def test_remove_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.remove(0), False)

    def test_reverse(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        linked_list.reverse()
        self.assertEqual(linked_list.head.data, 4)
        self.assertEqual(linked_list.head.next.data, 3)
        self.assertEqual(linked_list.head.next.next.data, 2)
        self.assertEqual(linked_list.head.next.next.next.data, 1)
        self.assertEqual(linked_list.tail.data, 0)

    def test_reverse_empty_list(self):
        linked_list = LinkedList()
        linked_list.reverse()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_extend(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 4)
        len1 = len(linked_list)

        linked_list1 = LinkedList()
        linked_list1.append(data='a')
        linked_list1.append(data='b')
        linked_list1.append(data='c')
        linked_list1.append(data='d')
        linked_list1.append(data='e')
        self.assertEqual(linked_list1.head.data, 'a')
        self.assertEqual(linked_list1.tail.data, 'e')
        len2 = len(linked_list1)

        linked_list.extend(linked_list1)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 'e')
        self.assertEqual(len(linked_list), len1 + len2)

    def test_extend_empty_first_list(self):
        linked_list = LinkedList()

        linked_list1 = LinkedList()
        linked_list1.append(data='a')
        linked_list1.append(data='b')
        linked_list1.append(data='c')
        linked_list1.append(data='d')
        linked_list1.append(data='e')
        len1 = len(linked_list)
        len2 = len(linked_list1)

        linked_list.extend(linked_list1)
        self.assertEqual(linked_list.head.data, 'a')
        self.assertEqual(linked_list.tail.data, 'e')
        self.assertEqual(len(linked_list), len1 + len2)

    def test_extend_empty_second_list(self):
        linked_list = LinkedList()

        linked_list1 = LinkedList()
        linked_list1.append(data='a')
        linked_list1.append(data='b')
        linked_list1.append(data='c')
        linked_list1.append(data='d')
        linked_list1.append(data='e')
        self.assertEqual(linked_list1.head.data, 'a')
        self.assertEqual(linked_list1.tail.data, 'e')

        linked_list1.extend(linked_list)
        self.assertEqual(linked_list1.head.data, 'a')
        self.assertEqual(linked_list1.tail.data, 'e')

    def test_extend_empty_both_list(self):
        linked_list = LinkedList()
        linked_list1 = LinkedList()

        linked_list1.extend(linked_list)
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 4)

        with self.assertRaises(UnboundLocalError) as error:
            del(linked_list)
            self.assertEqual(linked_list, None)

    def test_delete_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

        with self.assertRaises(UnboundLocalError) as error:
            del(linked_list)
            self.assertEqual(linked_list, None)

    def test_iter(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        counter = 0
        for data in linked_list:
            self.assertEqual(data, counter)
            counter += 1

    def test_iter_empty_list(self):
        linked_list = LinkedList()
        counter = 0
        for data in linked_list:
            self.assertEqual(data, counter)
            counter += 1

    def test_add(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 4)
        len1 = len(linked_list)

        linked_list1 = LinkedList()
        linked_list1.append(data='a')
        linked_list1.append(data='b')
        linked_list1.append(data='c')
        linked_list1.append(data='d')
        linked_list1.append(data='e')
        self.assertEqual(linked_list1.head.data, 'a')
        self.assertEqual(linked_list1.tail.data, 'e')
        len2 = len(linked_list1)

        linked_list2 = linked_list + linked_list1
        self.assertEqual(linked_list2.head.data, 0)
        self.assertEqual(linked_list2.tail.data, 'e')
        self.assertEqual(len(linked_list2), len1 + len2)

    def test_add_empty_first_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)
        len1 = len(linked_list)

        linked_list1 = LinkedList()
        linked_list1.append(data='a')
        linked_list1.append(data='b')
        linked_list1.append(data='c')
        linked_list1.append(data='d')
        linked_list1.append(data='e')
        self.assertEqual(linked_list1.head.data, 'a')
        self.assertEqual(linked_list1.tail.data, 'e')
        len2 = len(linked_list1)

        linked_list2 = linked_list + linked_list1
        self.assertEqual(linked_list2.head.data, 'a')
        self.assertEqual(linked_list2.tail.data, 'e')
        self.assertEqual(len(linked_list2), len1 + len2)

    def test_add_empty_second_list(self):
        linked_list = LinkedList()
        linked_list.append(data=0)
        linked_list.append(data=1)
        linked_list.append(data=2)
        linked_list.append(data=3)
        linked_list.append(data=4)
        self.assertEqual(linked_list.head.data, 0)
        self.assertEqual(linked_list.tail.data, 4)
        len1 = len(linked_list)

        linked_list1 = LinkedList()
        len2 = len(linked_list1)

        linked_list2 = linked_list + linked_list1
        self.assertEqual(linked_list2.head.data, 0)
        self.assertEqual(linked_list2.tail.data, 4)
        self.assertEqual(len(linked_list2), len1 + len2)

    def test_add_empty_both_list(self):
        linked_list = LinkedList()
        len1 = len(linked_list)

        linked_list1 = LinkedList()
        len2 = len(linked_list1)

        linked_list2 = linked_list + linked_list1
        self.assertEqual(linked_list2.head, None)
        self.assertEqual(linked_list2.tail, None)
        self.assertEqual(len(linked_list2), len1 + len2)
