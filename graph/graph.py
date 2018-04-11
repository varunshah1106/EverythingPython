from collections import defaultdict, deque, OrderedDict


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
        if not isinstance(neighbors, list) or \
                not isinstance(neighbors[0], tuple):
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
        if not self._directed:
            self.adjacency_list[data2].adjacent.pop(data1)
        return

    def is_connected(self, data1, data2):
        if data1 not in self.adjacency_list or \
                data2 not in self.adjacency_list:
            return False
        if data2 in self.adjacency_list[data1].adjacent:
            return True
        return False

    def topological_sort(self):
        if not self._directed:
            raise TypeError
        queue = deque()
        in_degrees = {}
        topological = []
        for i, vertex in self.adjacency_list.items():
            in_degrees[vertex.data] = in_degrees.get(vertex.data, 0)
            for neighbor in vertex.adjacent:
                in_degrees[neighbor] = in_degrees.get(neighbor, 0) + 1
        for i, vertex in self.adjacency_list.items():
            if in_degrees.get(vertex.data, -1) == 0:
                queue.append(vertex)
        while queue:
            vertex = queue.pop()
            topological.append(vertex.data)
            for neighbor in vertex.adjacent:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(self.adjacency_list[neighbor])
        return topological

    def dfs(self, node):
        if not self._directed:
            raise TypeError
        if node not in self.adjacency_list:
            return
        visited = OrderedDict()
        dfs_stack = [node]
        while dfs_stack:
            vertex = dfs_stack.pop()
            if vertex not in visited:
                visited[vertex] = True
                dfs_stack.extend(self.adjacency_list[vertex].adjacent.keys())
        return list(visited.keys())[1:]

    def bfs(self, node):
        if not self._directed:
            raise TypeError
        if node not in self.adjacency_list:
            return
        visited = OrderedDict()
        bfs_queue = deque(node)
        while bfs_queue:
            vertex = bfs_queue.popleft()
            if vertex not in visited:
                visited[vertex] = True
                bfs_queue.extend(self.adjacency_list[vertex].adjacent.keys())
        return list(visited.keys())[1:]
