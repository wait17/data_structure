# 列表形成栈
# class Stack:
#     def __init__(self, limit = 10):
#         self.stack = []
#         self.size = 0
#
#     def __str__(self):
#         return str(self.stack)
#
#     def da_yin(self):
#         self.__str__()
#
#     def push(self, data):
#         self.stack.append(data)
#         self.size += 1
#
#     def pop(self):
#         if self.stack:
#             temp = self.stack.pop()
#             self.size -= 1
#             return temp
#         else:
#             raise IndexError("pop from an empty stack")
#
#     def peek(self):  # 山峰
#         if self.stack:
#             return self.stack[-1]
#
#     def is_empty(self):
#         return not bool(self.stack)
#
#     def size1(self):
#         return self.size
#
# if __name__ == '__main__':
#     z = Stack(10)
#     z.push(1)
#     z.push(2)
#     z.push(3)
#     z.push(4)
#     z.push(5)
#     z.pop()
#     print(z.peek())
#     print(z.is_empty())
#     print(z.size1())
#     print(z.stack)
#
#
#
# # print(z.da_yin()) # 为什么为空

# 链表形成栈
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class LinkedStack:
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
            node = self.top  # 记录弹出的节点
            self.top = self.top.next
            self.size -= 1
            node.next = None
            return node.data
        else:
            raise IndexError("pop from an empty stack")

z = LinkedStack()
z.push(1)
# z.pop()
print(z.pop())
# print(z.top, z.size)

# 24,21