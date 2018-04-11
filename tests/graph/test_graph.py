from graph.graph import Graph
from graph.graph import Vertex

import unittest


class TestVertex(unittest.TestCase):

    def test_vertex_initialization(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))

    def test_vertex_initialization_invalid_data(self):
        with self.assertRaises(TypeError) as error:
            vertex = Vertex(data=None)

    def test_add_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        self.assertEqual(set(list(vertex.adjacent.keys())), set(['b']))
        self.assertEqual(vertex.adjacent.get('b'), 1)

    def test_add_neighbor_non_default_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b', weight=5)
        self.assertEqual(set(list(vertex.adjacent.keys())), set(['b']))
        self.assertEqual(vertex.adjacent.get('b'), 5)

    def test_add_neighbor_negative_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        with self.assertRaises(TypeError) as error:
            vertex.add_neighbor(data='b', weight=-5)

    def test_remove_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        self.assertEqual(set(list(vertex.adjacent.keys())), set(['b']))
        self.assertEqual(vertex.adjacent.get('b'), 1)
        self.assertEqual(vertex.remove_neighbor(data='b'), True)

    def test_remove_neighbor_key_error(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        self.assertEqual(set(list(vertex.adjacent.keys())), set(['b']))
        self.assertEqual(vertex.adjacent.get('b'), 1)
        with self.assertRaises(KeyError) as error:
            self.assertEqual(vertex.remove_neighbor(data='invalid_key'), False)

    def test_get_neighbor(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.get_neighbors(), ['b'])

    def test_get_neighbor_empty_adjacent_list(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.get_neighbors(), [])

    def test_get_weight(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        self.assertEqual(vertex.get_weight('b'), 1)
        vertex.add_neighbor(data='b', weight=5)
        self.assertEqual(vertex.get_weight('b'), 5)

    def test_get_weight_keyerror(self):
        vertex = Vertex(data='a')
        self.assertEqual(set(list(vertex.adjacent.keys())), set([]))
        vertex.add_neighbor(data='b')
        with self.assertRaises(KeyError) as error:
            self.assertEqual(vertex.get_weight('c'), None)

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
        self.assertEqual(set(list(vertex.get_neighbors())), set([]))
        data = [
            ('b', 3),
            ('c', 7),
            ('d'),
            tuple(['e'])
        ]
        vertex.add(neighbors=data)
        self.assertEqual(set(list(vertex.get_neighbors())),
                         set(['b', 'c', 'd', 'e']))
        self.assertEqual(vertex.get_weight('b'), 3)
        self.assertEqual(vertex.get_weight('c'), 7)
        self.assertEqual(vertex.get_weight('d'), 1)
        self.assertEqual(vertex.get_weight('e'), 1)

    def test_add_empty_tuple(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.add(neighbors=None), None)
        self.assertEqual(set(list(vertex.get_neighbors())), set([]))
        data = [
            tuple()
        ]
        self.assertEqual(vertex.add(neighbors=data), None)

    def test_add_tuple_not_int(self):
        vertex = Vertex(data='a')
        self.assertEqual(vertex.add(neighbors=None), None)
        self.assertEqual(set(list(vertex.get_neighbors())), set([]))
        data = [
            ('b', 'invalid weight'),
        ]
        with self.assertRaises(TypeError) as error:
            vertex.add(neighbors=data)


class TestUndirectedGraph(unittest.TestCase):

    def test_graph_initialization(self):
        graph = Graph()
        self.assertEqual(set(list(graph.adjacency_list.keys())), set([]))
        self.assertEqual(graph.adjacency_matrix, [])

    def test_add_vertex(self):
        graph = Graph()
        graph.add_vertex(data='a')
        self.assertEqual(set(list(graph.adjacency_list.keys())), set(['a']))
        graph.add_vertex(data=123)
        self.assertEqual(
            set(list(graph.adjacency_list.keys())), set([123, 'a']))

    def test_add_edge(self):
        graph = Graph()
        graph.add_vertex(data='a')
        graph.add_vertex(data=123)
        graph.add_edge(data1='a', data2=123, weight=3)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)
        self.assertEqual(graph.adjacency_list[123].adjacent['a'], 3)

    def test_add_edge_initial_data_none(self):
        graph = Graph()
        graph.add_edge(data1='a', data2=123, weight=3)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)

    def test_add(self):
        graph = Graph()
        data = ['a', 'b', 'c', 123, 456, 'd']
        graph.add(vertices=data)
        self.assertEqual(set(list(graph.adjacency_list.keys())),
                         set([123, 456, 'a', 'b', 'c', 'd']))

    def test_add_empty_list(self):
        graph = Graph()
        data = []
        graph.add(vertices=data)
        self.assertEqual(set(list(graph.adjacency_list.keys())), set([]))

    def test_add_invalid(self):
        graph = Graph()
        data = 'invalid data'
        with self.assertRaises(TypeError) as error:
            graph.add(vertices=data)

    def test_remove_vertex(self):
        graph = Graph()
        graph.add_edge(data1='a', data2=123, weight=3)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)
        graph.remove_vertex(123)
        self.assertEqual(set(list(graph.adjacency_list.keys())), set(['a']))
        self.assertEqual(
            set(list(graph.adjacency_list['a'].adjacent)), set([]))

    def test_remove_vertex_invalid(self):
        graph = Graph()
        graph.add_edge(data1='a', data2=123, weight=3)
        with self.assertRaises(KeyError) as error:
            graph.remove_vertex('invalid vertex')

    def test_remove_edge(self):
        graph = Graph()
        graph.add_edge(data1='a', data2=123, weight=3)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)
        graph.remove_edge('a', 123)
        self.assertEqual(
            set(list(graph.adjacency_list.keys())), set([123, 'a']))
        self.assertEqual(
            set(list(graph.adjacency_list['a'].adjacent)), set([]))
        self.assertEqual(
            set(list(graph.adjacency_list[123].adjacent)), set([]))

    def test_is_connected(self):
        graph = Graph()
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1=123, data2='c', weight=5)
        self.assertTrue(graph.is_connected(123, 'a'))
        self.assertTrue(graph.is_connected('a', 123))
        self.assertFalse(graph.is_connected('a', 'b'))
        self.assertFalse(graph.is_connected('a', 'c'))

    def test_topological_sort(self):
        graph = Graph(directed=False)
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1='b', data2=123, weight=2)
        graph.add_edge(data1='c', data2=123, weight=1)
        graph.add_edge(data1='c', data2='a', weight=1)
        with self.assertRaises(TypeError) as error:
            t = graph.topological_sort()

    def test_dfs(self):
        graph = Graph(directed=False)
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1='b', data2=123, weight=2)
        graph.add_edge(data1='c', data2=123, weight=1)
        graph.add_edge(data1='c', data2='a', weight=1)
        with self.assertRaises(TypeError) as error:
            t = graph.dfs(node='c')

    def test_bfs(self):
        graph = Graph(directed=False)
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1='b', data2=123, weight=2)
        graph.add_edge(data1='c', data2=123, weight=1)
        graph.add_edge(data1='c', data2='a', weight=1)
        with self.assertRaises(TypeError) as error:
            t = graph.bfs(node='c')


class TestDirectedGraph(unittest.TestCase):

    def test_graph_initialization(self):
        graph = Graph(directed=True)
        self.assertEqual(set(list(graph.adjacency_list.keys())), set([]))
        self.assertEqual(graph.adjacency_matrix, [])

    def test_add_vertex(self):
        graph = Graph(directed=True)
        graph.add_vertex(data='a')
        self.assertEqual(set(list(graph.adjacency_list.keys())), set(['a']))
        graph.add_vertex(data=123)
        self.assertEqual(
            set(list(graph.adjacency_list.keys())), set([123, 'a']))

    def test_add_edge(self):
        graph = Graph(directed=True)
        graph.add_vertex(data='a')
        graph.add_vertex(data=123)
        graph.add_edge(data1='a', data2=123, weight=3)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)
        self.assertEqual(graph.adjacency_list[123].adjacent, {})

    def test_remove_edge(self):
        graph = Graph(directed=True)
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1='b', data2=123, weight=2)
        graph.add_edge(data1='c', data2=123, weight=1)
        self.assertEqual(graph.adjacency_list['a'].adjacent[123], 3)
        self.assertEqual(graph.adjacency_list['b'].adjacent[123], 2)
        self.assertEqual(graph.adjacency_list['c'].adjacent[123], 1)
        graph.remove_edge('a', 123)
        self.assertEqual(graph.adjacency_list['a'].adjacent, {})
        graph.remove_edge('b', 123)
        self.assertEqual(graph.adjacency_list['b'].adjacent, {})
        graph.remove_edge('c', 123)
        self.assertEqual(graph.adjacency_list['c'].adjacent, {})

    def test_topological_sort(self):
        graph = Graph(directed=True)
        graph.add_edge(data1='a', data2=123, weight=3)
        graph.add_edge(data1='b', data2=123, weight=2)
        graph.add_edge(data1='c', data2=123, weight=1)
        graph.add_edge(data1='c', data2='a', weight=1)
        t = graph.topological_sort()
        self.assertEqual(t.index(123), 3)

    def test_topological_sort_empty_graph(self):
        graph = Graph(directed=True)
        t = graph.topological_sort()
        self.assertEqual(t, [])

    def test_dfs(self):
        graph = Graph(directed=True)
        graph.add_edge(data1='a', data2='b')
        graph.add_edge(data1='a', data2='c')
        graph.add_edge(data1='b', data2='d')
        graph.add_edge(data1='c', data2='e')
        t = graph.dfs(node='a')
        self.assertNotEqual(t.index('b'), 1)
        self.assertNotEqual(t.index('b'), 3)
        self.assertNotEqual(t.index('c'), 1)
        self.assertNotEqual(t.index('c'), 3)
        self.assertNotEqual(t.index('d'), 0)
        self.assertNotEqual(t.index('d'), 2)
        self.assertNotEqual(t.index('e'), 0)
        self.assertNotEqual(t.index('e'), 2)

    def test_dfs_empty_graph(self):
        graph = Graph(directed=True)
        t = graph.dfs(node='c')
        self.assertIsNone(t)

    def test_bfs(self):
        graph = Graph(directed=True)
        graph.add_edge(data1='a', data2='b')
        graph.add_edge(data1='a', data2='c')
        graph.add_edge(data1='b', data2='d')
        graph.add_edge(data1='c', data2='e')
        t = graph.bfs(node='a')
        self.assertNotEqual(t.index('b'), 2)
        self.assertNotEqual(t.index('b'), 3)
        self.assertNotEqual(t.index('c'), 2)
        self.assertNotEqual(t.index('c'), 3)
        self.assertNotEqual(t.index('d'), 0)
        self.assertNotEqual(t.index('d'), 1)
        self.assertNotEqual(t.index('e'), 0)
        self.assertNotEqual(t.index('e'), 1)

    def test_bfs_empty_graph(self):
        graph = Graph(directed=True)
        t = graph.bfs(node='c')
        self.assertIsNone(t)
