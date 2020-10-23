from typing import List


class Node:
    def __init__(self, data, next1=None):
        self.data = data
        self.next = next1

    def __repr__(self):
        return "node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head:
            emp = self.head
            while emp.next:
                emp = emp.next
            emp.next = Node(data)
        else:
            self.insert_head(data)

    def insert(self, i, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            emp = self.head
            j = 1
            pre = emp
            while j < i:
                pre = emp
                emp = emp.next
                j += 1
            pre.next = new_node
            new_node.next = emp

    def insert_list(self, i, object1: List):   # 链表下标(链表无下标,为了更好理解,这么记一下)从1开始
        if self.head is None:
            self.head = Node(object1[0])
            temp = self.head
            for j in object1[1:]:
                new_node = Node(j)
                temp.next = new_node
                temp = temp.next
        elif i == 0:
            raise IndexError("Index out of LinkList!")
        elif i == 1:
            old_head = self.head
            self.head = Node(object1[0])
            temp = self.head
            for j in object1[1:]:
                new_node = Node(j)
                temp.next = new_node
                temp = temp.next
            temp.next = old_head
        else:
            temp = self.head
            k = 1
            while temp:
                if k == i - 1:   # temp走到要插入位置的前一个
                    last = temp.next
                    temp.next = Node(object1[0])
                    for a1 in object1[1:]:
                        new_node = Node(a1)
                        temp.next.next = new_node
                        temp = temp.next
                    temp.next.next = last
                    break
                elif temp.next is None:   # 输入的 i 值太大, 链表没有那么多节点的情况
                    temp.next = Node(object1[0])
                    for a2 in object1[1:]:
                        new_node = Node(a2)
                        temp.next.next = new_node
                        temp = temp.next
                    break
                k += 1
                temp = temp.next

    def delete_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        else:
            return "空链表"

    def delete_tail(self):
        if self.head:
            temp = self.head
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            return "空链表"

    def reverse(self):
        if self.head:
            pre = None
            temp = self.head
            while temp:
                next_node = temp.next
                temp.next = pre
                pre = temp
                temp = next_node
            self.head = pre
        else:
            raise Exception("空链表")

    def __getitem__(self, item):
        current = self.head
        if current is None:
            raise Exception("空链表")
        for _ in range(1, item):   # 循环item - 1次(走item - 1步)
            current = current.next
        return current

    def get(self, index):
        return self.__getitem__(index)

    def __set__(self, index, value):
        current = self.head
        if current is None:
            raise Exception("空链表")
        for _ in range(1, index):
            current = current.next
        current.data = value

    def set(self, index, value):
        return self.__set__(index, value)

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += "{}-->".format(current)
            current = current.next
        return string_repr + "END"


ll = LinkList()
ll.insert_head(1)
ll.append(2)
ll.insert(2, 3)
ll.insert_list(2, [4, 5, 6])
ll.delete_head()   # 头为空时不会返回"空链表",只有EMD???  因为return得打印才能显示,光调用,不打印就不会打印出东西来 结果显示的END是类里面打印方法的结果
ll.delete_tail()
print(ll.get(3))
ll.set(1, 9)
print(ll)
ll.reverse()
print(ll)
