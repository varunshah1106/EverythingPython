class Node(object):

    def __init__(self, data):
        if data is None:
            raise ValueError('data can not be None')
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        node = Node(data)
        _temp = self.root
        while _temp:
            if data < _temp.data:
                if not _temp.left:
                    _temp.left = node
                    return
                else:
                    _temp = _temp.left
            else:
                if not _temp.right:
                    _temp.right = node
                    return
                else:
                    _temp = _temp.right

    def find(self, data, node):
        if node is None or data is None:
            return
        if data == node.data:
            return node
        elif data < node.data:
            return self.find(data, node.left)
        else:
            return self.find(data, node.right)

    def delete(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self.delete(data, node.left)
        elif data > node.data:
            node.right = self.delete(data, node.right)
        else:
            if node.left and node.right:
                temp = self.findInorderSuccessor(node.right)
                node.data = temp.data
                node.right = self.delete(temp.data, node.right)
            else:
                if node.left:
                    left = node.left
                    node.left = None
                    return left
                else:
                    right = node.right
                    node.right = None
                    return right
        return node

    @staticmethod
    def findInorderSuccessor(node):
        while node.left:
            node = node.left
        return node


    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
        return

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)
        return

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
        return

    def get_min(self, node):
        if not node:
            return None
        _temp = node
        while _temp.left:
            _temp = _temp.left
        return _temp.data

    def get_max(self, node):
        if not node:
            return None
        _temp = node
        while _temp.right:
            _temp = _temp.right
        return _temp.data
