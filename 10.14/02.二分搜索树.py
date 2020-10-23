# 创建节点类
# 创建树类
# 1 属性
# 2 打印
# 3 插入(私有方法+方法)
# 4 删除
# 5 节点重排
# 6 查找值对应的节点
# 7 查找值最大的节点
# 8 判断是否为空
# 9 判断是否为右孩子
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
            node.parent = parent_node   # 为了维护父节点属性,并非参与循环

    def insert(self, *values):
        for value in values:
            self.__insert(value)

    def remove(self, data):   # 移除根节点时正常执行代码
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
                temp = self.get_max(node.left)   # 删除(有两个孩子的)根节点直接走这一部分
                self.remove(temp.data)
                node.data = temp.data

    def reassign_nodes(self, node, new_children):
        if new_children is not None:
            new_children.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:   # 专为只有根节点的树准备
            self.root = new_children

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
            return node   # 无相应值时,返回None, 因为找不到,所以会一直找到空的位置(此时循环也会进不去),故返回None

    def is_right(self, node):   # 逻辑简单粗暴, 判断当前节点是不是它父亲的右孩子
        return node == node.parent.right

    def get_max(self, node=None):   # 查找到当前节点以及它的后代当中最大的值
        if node is None:   # ???
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node


bst = BinarySearchTree()
bst.insert(8, 1, 7, 9, 10, 5, 6, 8, 4)
# print(bst)
# bst.remove(9)
# bst.remove(5)
# print(bst.is_empty())
# print(bst.is_right(bst.search(5)))
# print(bst.get_max(bst.root))
# print(bst.search(5))
print(bst)
