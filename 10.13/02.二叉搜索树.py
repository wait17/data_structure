# 二分搜索树/二叉搜索树
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
        return pformat({"%s" % (self.data) : (self.left, self.right)}, indent=1)


class BinarySearchTree:   # BST
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        return False
        # return True if self.root is None else False

    def __insert(self, value):
        node = Node(value)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right
            node.parent = parent_node

    def insert(self, *values):   # 不定长参数
        for value in values:
            self.__insert(value)

    def search(self, value):   # 为什么不存在打印出None(怎么做到的)
        if self.is_empty():
            raise Exception("空树!")
        else:
            node = self.root
            while node and node.data != value:
                if value < node.data:
                    node = node.left
                elif value > node.data:
                    node = node.right
            return node

    def is_right(self, node):
        return node == node.parent.right

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:   # 找父亲
            new_children.parent = node.parent
        if node.parent is not None:   # 找孩子
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def remove(self, value):
        if self.root is None:
            raise Exception("空树")
        else:
            node = self.search(value)
            if node is not None:
                if node.left is None and node.right is None:
                    self.__reassign_nodes(node, None)
                elif node.left is None:
                    self.__reassign_nodes(node, node.right)
                elif node.right is None:
                    self.__reassign_nodes(node, node.left)
                else:
                    temp = self.get_max(node.left)
                    self.remove(temp.data)
                    node.data = temp.data

    def get_max(self, left):
        pass


bst = BinarySearchTree()
# print(bst.is_empty())
bst.insert(8, 1, 3, 5, 6)
print(bst)
bst.remove(3)
# print(bst.search(4))
print(bst)
