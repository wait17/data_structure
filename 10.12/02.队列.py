"""
:Author:Ms.Ren
:Create: 2020/10/12 11:51
"""


# class Queue:
#     def __init__(self):
#         self.entries = []
#         self.size = 0
#
#     def enqueue(self, data):
#         self.entries.append(data)
#         self.size += 1
#
#     def dequeue(self):
#         item = self.entries[0]
#         self.entries = self.entries[1:]
#         self.size -= 1
#         return item
#
#     def get(self, index):
#         item = self.entries[index]
#         return item
#
#     def __str__(self):
#         printed = "<" + str(self.entries)[1:-1] + ">"
#         return printed
#
#     def set(self, index, data):
#         self.entries[index] = data
#
#     def front(self):
#         return self.entries[0]
#
#     def cap(self):
#         return self.size
#
#     def reverse(self):
#         self.entries.reverse()
#         printed = "<" + str(self.entries)[1:-1] + ">"
#         return printed
#
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.dequeue()
# # q.dequeue()
# # print(q.get(2))
# q.set(2,5)
# print(q)
# print(q.reverse())
# # print(q.cap())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def put(self, data):   # enqueue 入队
        node = Node(data)
        if self.front:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node
        self.size += 1

    def pop(self):   # dequeue 出队
        if self.size == 0:
            raise Exception("空队列")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.size -= 1
            return temp

    def __repr__(self):
        curr = self.front
        string_repr = ""
        while curr:
            string_repr += "{}-->".format(curr)
            curr = curr.next
        return string_repr + "END"

q = LinkedQueue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.pop()
print(q)