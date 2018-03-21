from __future__ import print_function
from data_structures.linked_list import LinkedList

import unittest


class TestLinkedList(unittest.TestCase):
    def test(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert('test text')
        self.assertEqual(len(ll), 2)
        ll.insert(10000)
        ll.insert(-1000)
        ll.insert('a')
        ll.insert('qwerty')
        print (ll)
