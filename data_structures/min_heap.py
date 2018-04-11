class MinHeap(object):

    def __init__(self):
        self.heapList = []
        self.size = 0

    def heapify(self, array):
        if not isinstance(array, list):
            raise TypeError
        self.heapList = array
        self.size = len(array)
        n = self.size
        for i in range(n // 2, -1, -1):
            self._percolate_down(i)
        return

    def minimum(self):
        if self.size == 0:
            return None
        return self.heapList[0]

    def _bubble_up(self, index):
        while index != 0:
            parent = (index - 1) // 2
            if self.heapList[parent] > self.heapList[index]:
                self.heapList[parent], self.heapList[index] = \
                    self.heapList[index], self.heapList[parent]
            index = parent
        return

    def _percolate_down(self, index):
        while (index * 2 + 1) < self.size:
            min_child = self._minimum_child(index)
            if self.heapList[index] > self.heapList[min_child]:
                self.heapList[index], self.heapList[min_child] = \
                    self.heapList[min_child], self.heapList[index]
            index = min_child
        return

    def _minimum_child(self, index):
        child1 = self.heapList[2 * index +
                               1] if (2 * index + 1) < self.size else None
        child2 = self.heapList[2 * index +
                               2] if (2 * index + 2) < self.size else None
        return (2 * index + 1) if (child1 < child2) else (2 * index + 2)

    def insert(self, data):
        if data is None or not (isinstance(data, str) or
                                isinstance(data, int)):
            return False
        self.heapList.append(data)
        self.size += 1
        self._bubble_up(self.size - 1)
        return True

    def remove(self, index):
        if not isinstance(index, int):
            raise TypeError
        if index >= self.size:
            raise IndexError
        self.heapList[index] = self.heapList[-1]
        self.heapList.pop()
        self.size -= 1
        self._percolate_down(index)
        return

    def deleteMin(self):
        return self.remove(0)
