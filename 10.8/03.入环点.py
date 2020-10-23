# from typing import Optional    # 可选择类型的类型注解模块
# 类型注解只是提供了一种提示(使用时可以提示传入的参数的类型),实际上对运行没有任何影响


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


def detectCirclePoint(head: Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node3

    print(detectCirclePoint(node1))