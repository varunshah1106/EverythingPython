from graph.graph import Graph
from graph.graph import Vertex

import unittest


class TestVertex(unittest.TestCase):

    def test_vertex_initialization(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])

    def test_vertex_initialization_invalid_data(self):
        with self.assertRaises(TypeError) as error:
            vertex = Vertex(data=None)

    def test_add_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.adjacent.keys(), ['b'])
        self.assertEqual(vertex.adjacent.get('b'), 1)

    def test_add_neighbor_non_default_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b', weight=5)
        self.assertEqual(vertex.adjacent.keys(), ['b'])
        self.assertEqual(vertex.adjacent.get('b'), 5)

    def test_add_neighbor_negative_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        with self.assertRaises(TypeError) as error:
            vertex.add_neighbor(data='b', weight=-5)

    def test_remove_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.adjacent.keys(), ['b'])
        self.assertEqual(vertex.adjacent.get('b'), 1)
        self.assertEqual(vertex.remove_neighbor(data='b'), True)

    def test_remove_neighbor_key_error(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.adjacent.keys(), ['b'])
        self.assertEqual(vertex.adjacent.get('b'), 1)
        with self.assertRaises(KeyError) as error:
            self.assertEqual(vertex.remove_neighbor(data='invalid_key'), False)

    def test_get_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.get_neighbors(), ['b'])

    def test_get_neighbor_empty_adjacent_list(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.get_neighbors(), [])

    def test_get_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.get_weight('b'), 1)
        vertex.add_neighbor(data='b', weight=5)
        self.assertEqual(vertex.get_weight('b'), 5)

    def test_get_weight_keyerror(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.adjacent.keys(), [])
        vertex.add_neighbor(data='b')
        with self.assertRaises(KeyError) as error:
            self.assertEqual(vertex.get_weight('c'), None)

    def test_add(self):
        vertex = Vertex(data='a')
        self.assertIsNone(vertex.add(neighbors=[]))
        self.assertEqual(vertex.get_neighbors(), [])

    def test_add_neighbors_not_list(self):
        vertex = Vertex(data='a')
        with self.assertRaises(TypeError) as error:
            self.assertIsNone(vertex.add(neighbors='invalid_data'))

    def test_add_neighbors_not_tuple(self):
        vertex = Vertex(data='a')
        with self.assertRaises(TypeError) as error:
            self.assertIsNone(vertex.add(neighbors=['invalid_data']))

    def test_add(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.add(neighbors=None), None)
        self.assertListEqual(sorted(vertex.get_neighbors()), [])
        data = [
            ('b', 3),
            ('c', 7),
            ('d'),
            tuple(['e'])
        ]
        vertex.add(neighbors=data)
        self.assertListEqual(sorted(vertex.get_neighbors()), ['b', 'c', 'd', 'e'])
        self.assertEqual(vertex.get_weight('b'), 3)
        self.assertEqual(vertex.get_weight('c'), 7)
        self.assertEqual(vertex.get_weight('d'), 1)
        self.assertEqual(vertex.get_weight('e'), 1)

    def test_add_empty_tuple(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.add(neighbors=None), None)
        self.assertListEqual(sorted(vertex.get_neighbors()), [])
        data = [
            tuple()
        ]
        self.assertEqual(vertex.add(neighbors=data), None)

    def test_add_tuple_not_int(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.add(neighbors=None), None)
        self.assertListEqual(sorted(vertex.get_neighbors()), [])
        data = [
            ('b', 'invalid weight'),
        ]
        with self.assertRaises(TypeError) as error:
            vertex.add(neighbors=data)
