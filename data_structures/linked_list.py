class Node(object):

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def __add__(self, second):
        new_list = LinkedList()
        node = self.head
        while node:
            new_list.insert(node.data)
            node = node.next
        new_list.extend(second)
        return new_list

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __del__(self):
        self.head = None
        self.tail = None
        return

    def __str__(self):
        node = self.head
        string = ''
        while node:
            string = string + str(node.data) + ' --->'
            node = node.next
        return string[:-5]

    def __len__(self):
        return self.__length

    def extend(self, other):
        self.tail.next = other.head
        other.head.previous = self.tail
        self.tail = other.tail
        return

    def reverse(self):
        node = self.head
        while node:
            node.previous, node.next = node.next, node.previous
            node = node.next
        self.head, self.tail = self.tail, self.head
        return

    def length(self):
        return self.__length

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return -1

    def remove(self, data):
        if not self.head:
            return False
        node = self.head
        counter = 0
        while node:
            if node.data == data:
                self.removeAt(index=counter)
                return True
            else:
                counter += 1
                node = node.next
        return False

    def removeAt(self, index):
        if index >= self.__length:
            raise IndexError
        if index == 0:
            self.head.next.previous = None
            self.head = self.head.next
            self.__length -= 1
            return True
        previous_node = self.nodeAt(index - 1)
        node = previous_node.next
        if node == self.tail:
            previous_node.next = None
            self.tail = previous_node
            self.__length -= 1
        else:
            previous_node.next = node.next
            node.next.previous = node.previous
            self.__length -= 1
        return True

    def valueAt(self, index):
        if index >= self.__length:
            raise IndexError
        node = self.head
        for i in range(index):
            node = node.next
        return node.data

    def indexOf(self, data):
        pointer = self.head
        counter = 0
        while pointer:
            if pointer.data == data:
                return counter
            else:
                counter += 1
                pointer = pointer.next
        return -1

    def nodeAt(self, index):
        if index >= self.__length or index < 0:
            raise IndexError
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.previous = self.tail
        self.tail = node
        self.__length += 1
        return

    def insert(self, data, index):
        node = Node(data)
        if index < 0 or index > self.__length:
            raise IndexError
        if not self.head:
            self.head = node
            self.tail = node
            self.__length += 1
            return
        if index == 0:
            node.next = self.head
            self.head.previous = node
            self.head = node
            self.__length += 1
            return
        if index == self.__length:
            self.append(data)
            return
        previous_node = self.nodeAt(index - 1)
        previous_node.next.previous = node
        node.next = previous_node.next
        node.previous = previous_node
        previous_node.next = node
        self.__length += 1
        return
