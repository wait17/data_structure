# -->平衡树(AVL) 红黑树   --> 都能把树做平衡
# 完全二叉树(最后一个节点之前的节点都是齐全的), 满二叉树
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
            node.parent = parent_node

    def insert(self, *values):
        for value in values:
            self.__insert(value)

    def remove(self, data):
        if self.is_empty():
            raise Exception("空树")
        else:
            node = self.search(data)
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

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def search(self, data):
        if self.is_empty():
            raise Exception("空树")
        else:
            node = self.root
            while node and node.data != data:
                if data < node.data:
                    node = node.left
                else:
                    node = node.right
            return node

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def is_right(self, node):
        return node == node.parent.right

    def get_max(self, node):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

    def pre_order_traverse(self, node):
        if node is None:
            return None
        print(node.data, end="\t")
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    def in_order_traverse(self, node):
        if node is None:
            return None
        self.in_order_traverse(node.left)
        print(node.data, end="\t")
        self.in_order_traverse(node.right)

    def post_order_traverse(self, node):
        if node is None:
            return None
        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print(node.data, end="\t")

    def pre_order_traverse2(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.data, end="\t")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def in_order_traverse2(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.data, end="\t")
                node = node.right

    def post_order_traverse2(self, node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)   # stack2获得逆序(先弹的后入栈,后弹的先入栈)
        while stack2:
            print(stack2.pop().data, end="\t")


bst = BinarySearchTree()
bst.insert(8, 3, 1, 6, 10, 9, 5, 8)
# bst.remove(3)
# print(bst)
# print(bst.is_empty())
# print(bst.is_right(bst.search(6)))
# print(bst.get_max(bst.search(3)))
# bst.pre_order_traverse(bst.root)
# bst.pre_order_traverse2(bst.root)
# bst.in_order_traverse(bst.root)
# bst.in_order_traverse2(bst.root)
# bst.post_order_traverse(bst.root)
bst.post_order_traverse2(bst.root)
