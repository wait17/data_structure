class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def get_parent(self, item):   # 找到值为item的节点的父节点
        if self.root.data == item:
            return None   # 没有父节点
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == item:
                return pop_node
            if pop_node.right.data == item:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None


t = Tree()
t.add(1)
t.add(2)
t.add(3)
# print(t.root.left)
print(t.get_parent(4))
