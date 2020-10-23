"""
:Author:Ms.Ren
:Create: 2020/10/10 11:08
"""
# 虚拟节点/哑节点 203, 24, 21
# 203 删除指定值

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"node({self.data})"
#
#
# def remove_elements(head: Node, value):
#     if head:
#         current = head
#         temp = head
#         i = 0
#         while current:
#             i += 1
#             if current.data == value:
#                 current = current.next
#                 temp = temp.next
#                 if i == 1:
#                     head = current
#     else:
#         raise Exception("空链表")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


def remove_elements(head: Node, value: int):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next:
        if current.next.data == value:
            temp = current.next
            current.next = current.next.next
            temp.next = None
        else:
            current = current.next
    head = dummy.next
    curr = head
    string_repr = ""
    while curr:
        string_repr += "{}-->".format(curr)
        curr = curr.next
    return string_repr + "END"

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(5)
    node6 = Node(6)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    
    print(remove_elements(node1, 2))