from collections import defaultdict


class Vertex(object):

    def __init__(self, data):
        if data is None:
            raise TypeError
        self.data = data
        self.adjacent = defaultdict()
        return

    def add(self, neighbors):
        if not neighbors:
            return
        if not isinstance(neighbors, list) or not isinstance(neighbors[0], tuple):
            raise TypeError
        for tup in neighbors:
            if not tup:
                return
            elif isinstance(tup, str):
                self.add_neighbor(tup)
            elif len(tup) == 1:
                self.add_neighbor(tup[0])
            else:
                if not isinstance(tup[1], int):
                    raise TypeError
                else:
                    self.add_neighbor(tup[0], tup[1])
        return

    def add_neighbor(self, data, weight=1):
        if weight < 1:
            raise TypeError
        self.adjacent[data] = weight
        return

    def remove_neighbor(self, data):
        try:
            return self.adjacent.pop(data)
        except KeyError:
            raise

    def get_neighbors(self):
        return list(self.adjacent.keys())

    def get_weight(self, key):
        try:
            return self.adjacent[key]
        except KeyError:
            raise


class Graph(object):

    def __init__(self, directed=False):
        self.adjacency_list = defaultdict()
        self.adjacency_matrix = []
        self._directed = directed

    def add(self, vertices):
        if not isinstance(vertices, list):
            raise TypeError
        for vertex in vertices:
            self.add_vertex(data=vertex)

    def add_vertex(self, data):
        self.adjacency_list[data] = Vertex(data=data)
        return

    def remove_vertex(self, data):
        try:
            self.adjacency_list.pop(data)
        except KeyError:
            raise
        for key, vertex in self.adjacency_list.items():
            vertex.remove_neighbor(data)
        return

    def add_edge(self, data1, data2, weight=1):
        if data1 not in self.adjacency_list:
            self.add_vertex(data=data1)
        if data2 not in self.adjacency_list:
            self.add_vertex(data=data2)
        self.adjacency_list[data1].add_neighbor(data=data2, weight=weight)
        if not self._directed:
            self.adjacency_list[data2].add_neighbor(data=data1, weight=weight)
        return

    def remove_edge(self, data1, data2):
        self.adjacency_list[data1].adjacent.pop(data2)
        self.adjacency_list[data2].adjacent.pop(data1)
        return

    def _convert_list_to_matrix(self):
        pass

    def _convert_matrix_to_list(self):
        pass

    def is_connected(self, data1, data2):
        if data1 not in self.adjacency_list or data2 not in self.adjacency_list:
            return False
        if data2 in self.adjacency_list[data1].adjacent:
            return True
        return False
