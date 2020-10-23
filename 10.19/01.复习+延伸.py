# 计算阶乘(递归方法)
def mul(n):
    if n == 1 or n == 0:   # 递归出口
        return 1
    return mul(n - 1) * n   # 递归表达式


# 青蛙跳台阶(n个台阶,青蛙每次跳一阶或两阶,有多少种跳法)
def jump(n):
    if n == 1 or n == 2:
        return n
    return jump(n - 1) + jump(n - 2)


print(jump(5))


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
            pass

    def reassign(self, node, new_children):
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

    def is_empty(self):
        return True if self.root is None else False

    def pre_order_traverse(self, node):
        if node is None:
            return None
        print(node.data)
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

    def in_order_traverse(self, node):
        if node is None:
            return None
        self.in_order_traverse(node.left)
        print(node.data)
        self.in_order_traverse(node.right)

    def post_order_traverse(self, node):
        if not node:
            return None
        self.post_order_traverse(node.left)
        self.post_order_traverse(node.right)
        print(node.data)

    def pre_order_stack(self, node):
        stack = [node]
        while len(stack) > 0:
            print(node.data, end="\t")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def in_order_stack(self, node):
        stack = []
        pass
