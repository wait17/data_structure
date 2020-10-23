# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):  # 表示, 代表
#         return "node({})".format(self.data)
#
#
# def is_circle(head: Node):
#     fast = head
#     slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             return True
#     return False
#
# def detectSirclePoint(head: Node):  # 自己的函数,判断了是否为环,再调用查找入环点函数
#     fast = head
#     slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             break  # 不终止,直接写下边语句也可以
#
#     slow = head
#     while slow != fast:
#         slow = slow.next
#         fast = fast.next
#     return slow
#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     node7 = Node(7)
#     node8 = Node(8)
#
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node6
#     node6.next = node7
#     node7.next = node8
#     node8.next = node4
#
#     print(is_circle(node1))
#     print(detectSirclePoint(node1))

class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("索引越界")
        else:
            if  index >= len(self.array) or self.size >= len(self.array):
                self.addCapacity()
            for i in range(self.size - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = element
            self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("数组越界")
        else:
            if  self.size >= len(self.array):  # index >= len(self.array) or     前边代码中的">"更保险
                self.addCapacity()
            for i in range(index, self.size):
                self.array[i] = self.array[i + 1]  # 列表放满时会下标越界 因为i+1 = self.size > max(index),所以下标越界  --> 处理方法,如上(扩容) -- 待调整
            self.size -= 1

    def addCapacity(self):
        new_array = [None] * len(self.array) * 2  # 乘2只是随意给定,可以扩容为其他长度
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

if __name__ == '__main__':
    a = Array(5)
    a.insert(0,1)
    a.insert(1,2)
    a.insert(2,3)
    a.insert(3,4)
    a.insert(4,5)
    a.remove(1)

    print(a.array)
    print(a.size)