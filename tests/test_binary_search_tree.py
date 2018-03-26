from data_structures.binary_search_tree import BinarySearchTree

import unittest
import sys


class StdOutMock(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s.strip())

    def __str__(self):
        return "".join(self.data)


class TestBinarySearchTree(unittest.TestCase):

    def test_initiation(self):
        bst = BinarySearchTree(data=5)
        self.assertEqual(bst.root.data, 5)

    def test_initiation_invalid(self):
        with self.assertRaises(ValueError) as error:
            bst = BinarySearchTree(data=None)

    def test_insert_valid(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        self.assertEqual(bst.root.left.data, 3)
        bst.insert(7)
        self.assertEqual(bst.root.right.data, 7)
        bst.insert(1)
        self.assertEqual(bst.root.left.left.data, 1)
        bst.insert(2)
        self.assertEqual(bst.root.left.left.right.data, 2)
        bst.insert(9)
        self.assertEqual(bst.root.right.right.data, 9)

    def test_insert_invalid(self):
        bst = BinarySearchTree(data=5)
        with self.assertRaises(ValueError) as error:
            bst.insert(data=None)

    def test_find_successful(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.find(5, bst.root), bst.root)
        self.assertEqual(bst.find(1, bst.root), bst.root.left.left)

    def test_find_successful_different_node(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.find(1, bst.root.left), bst.root.left.left)
        self.assertEqual(bst.find(9, bst.root.right), bst.root.right.right)
        self.assertIsNone(bst.find(9, bst.root.left))

    def test_find_unsuccessful(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        self.assertEqual(bst.find(-1, bst.root), None)

    def test_get_min(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.get_min(bst.root), 1)

    def test_get_min_different_node(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.get_min(bst.root.right), 7)

    def test_get_min_empty_bst(self):
        bst = BinarySearchTree(data=5)
        self.assertIsNone(bst.get_min(bst.root.right))

    def test_get_max(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.get_max(bst.root), 9)

    def test_get_max_different_node(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        self.assertEqual(bst.get_max(bst.root.left), 3)

    def test_get_max_empty_bst(self):
        bst = BinarySearchTree(data=5)
        self.assertIsNone(bst.get_max(bst.root.right))

    def test_find_inorder_successor(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)
        self.assertEqual(bst.findInorderSuccessor(bst.root.right).data, 6)
        self.assertEqual(bst.findInorderSuccessor(bst.root).data, 1)
        self.assertEqual(bst.findInorderSuccessor(bst.root.left).data, 1)
        self.assertEqual(bst.findInorderSuccessor(bst.root.left.left).data, 1)

    def test_delete_successful_left_subtree(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(4)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)

        self.assertIsNotNone(bst.delete(3, bst.root))
        self.assertIsNone(bst.root.left.right)
        self.assertEqual(bst.root.left.data, 4)

        self.assertIsNotNone(bst.delete(4, bst.root))
        self.assertEqual(bst.root.left.data, 1)

        self.assertIsNotNone(bst.delete(1, bst.root))
        self.assertIsNotNone(bst.delete(2, bst.root))

    def test_delete_successful_right_subtree(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)
        self.assertIsNotNone(bst.delete(5, bst.root))
        self.assertEqual(bst.root.data, 6)
        self.assertEqual(bst.root.right.data, 7)
        self.assertEqual(bst.root.right.right.data, 9)
        self.assertIsNone(bst.root.right.left)
        self.assertIsNone(bst.root.right.right.left)

        self.assertIsNotNone(bst.delete(9, bst.root))
        self.assertEqual(bst.root.data, 6)
        self.assertEqual(bst.root.right.data, 7)
        self.assertIsNone(bst.root.right.left)
        self.assertIsNone(bst.root.right.right)

    def test_delete_node_is_none(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)
        self.assertEqual(bst.delete(3, None), None)

    def test_inorder(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.inorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '1235679')

    def test_inorder_single_node(self):
        bst = BinarySearchTree(data=5)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.inorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '5')

    def test_preorder(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.preorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '5312769')

    def test_preorder_single_node(self):
        bst = BinarySearchTree(data=5)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.preorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '5')

    def test_postorder(self):
        bst = BinarySearchTree(data=5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(1)
        bst.insert(2)
        bst.insert(9)
        bst.insert(6)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.postorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '2136975')

    def test_postorder_single_node(self):
        bst = BinarySearchTree(data=5)

        stdout_org = sys.stdout
        stdout_mock = StdOutMock()
        try:
            sys.stdout = stdout_mock
            bst.postorder(bst.root)
        finally:
            sys.stdout = stdout_org

        self.assertEqual(str(stdout_mock), '5')
