# 合并两个有序链表
class Node:
    def __init__(self, data=0, next1=None):
        self.data = data
        self.next = next1

    def __repr__(self):
        return "node({})".format(self.data)


# def merge_two_lists(h1, h2):
#     dummy = Node()
#     current = dummy
#     while h1 or h2:
#         if h1.data <= h2.data:
#             current.next = Node(h1.data)
#             h1 = h1.next
#         else:
#             current.next = Node(h2.data)
#             h2 = h2.next
#         current = current.next
#         if h1 is None:
#             current.next = h2
#             break
#         if h2 is None:
#             current.next = h1
#     head = dummy.next
#     curr = head
#     string_repr = ""
#     while curr:
#         string_repr += "{}-->".format(curr)
#         curr = curr.next
#     return string_repr + "END"


# def merge_two_lists2(h1, h2):
#     dummy = Node()
#     current = dummy
#     while h1 and h2:
#         if h1.data <= h2.data:
#             current.next = Node(h1.data)
#             h1 = h1.next
#         else:
#             current.next = Node(h2.data)
#             h2 = h2.next
#         current = current.next
#     if h1 is None:
#         current.next = h2
#     elif h2 is None:
#         current.next = h1
#     head = dummy.next
#     curr = head
#     string_repr = ""
#     while curr:
#         string_repr += "{}-->".format(curr)
#         curr = curr.next
#     return string_repr + "END"
#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(3)
#     node3 = Node(3)
#     node4 = Node(9)
#     node5 = Node(2)
#     node6 = Node(6)
#     node7 = Node(8)
#     node8 = Node(9)
#
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = None
#     node5.next = node6
#     node6.next = node7
#     node7.next = node8
#     node8.next = None
#
#     print(merge_two_lists2(node1, node5))


# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def __str__(self):
#         return str(self.stack)
#
#     def push(self, data):
#         self.stack.append(data)
#         self.size += 1
#
#     def pop(self):
#         self.stack.pop()
#         self.size -= 1
#
#     def size1(self):
#         return self.size
#
#     def is_empty(self):
#         return not bool(self.stack)
#
#     def peek(self):
#         return self.stack[-1]
#
# s = Stack()
# print(s.is_empty())
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# print(s.__str__())
# s.pop()
# print(s.peek())
# print(s.is_empty())
# print(s.size1())
# print(s.__str__())


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            pass
        else:
            raise Exception("空栈")
