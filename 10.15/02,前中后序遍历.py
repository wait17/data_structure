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
        return pformat({"%s" % self.data : (self.left, self.right)}, indent=1)


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
                self.reassign_nodes(node, None)
            elif node.left is None:
                self.reassign_nodes(node, node.right)
            elif node.right is None:
                self.reassign_nodes(node, node.left)
            else:
                temp = self.get_max(node.left)
                self.remove(temp.data)
                node.data = temp.data

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

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def is_right(self, node):
        return node == node.parent.right

    def get_max(self, node=None):   # ???
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

    def get_min(self, node=None):
        pass

    def pre_order_traverse(self, node):
        if not node:
            return None
        print(node.data, end="\t")
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    def pre_order_traverse2(self, node):   # 栈里的顺序: 根右左
        stack = [node]
        while len(stack) > 0:
            print(node.data, end="\t")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def in_order_traverse(self, node):
        if not node:
            return None
        self.in_order_traverse(node.left)
        print(node.data, end="\t")
        self.in_order_traverse(node.right)

    def in_order_traverse2(self, node):   # 栈里的顺序: 左--根--右
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.data, end="\t")
                node = node.right

    def post_order_traverse(self, node):
        if not node:
            return None
        self.post_order_traverse(self.left)
        self.post_order_traverse(self.right)
        print(node.data)


bst = BinarySearchTree()
bst.insert(4, 3, 5, 7, 9, 2, 6, 8)
# print(bst)
# # bst.remove(9)
# bst.remove(4)
# print(bst)
# print(bst.search(7))
# print(bst.is_empty())
# print(bst.get_max())
# print(bst.is_right(bst.search(8)))
# bst.insert(7, 6, 9, 8, 10)
# print(bst)
# print(bst.search(9))
# print(bst.get_max(bst.search(9)))
# bst.remove(7)
# bst.insert(4, 3)
# bst.remove(4)
# bst.insert(4, 3, 5)
# bst.pre_order_traverse(bst.search(4))
bst.pre_order_traverse2(bst.search(4))
# bst.in_order_traverse(bst.root)
# bst.in_order_traverse2(bst.root)
# print(bst)
