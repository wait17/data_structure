from pprint import pformat


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % self.data: (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def __insert(self, data):
        node = Node(data)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right


    def level_order_traverse(self, node):
        from queue import Queue
        queue = Queue()
        queue.put(node)
        while not queue.empty():
            node = queue.get()
            print(node.data)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

    def is_empty(self):
        # if self.root is None:
        #     return True
        # return False
        return True if self.root is None else False
