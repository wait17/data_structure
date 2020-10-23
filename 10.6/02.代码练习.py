from typing import List

# ###########################练习加笔记###########################

# 链表:
# 1.增(插入)
# 1-1 插入单独数据
# 1-1-1 从头插入
# 1-1-2 从尾插入
# 1-1-3 从中间插入
# 1-2 插入列表(目前所学为将列表直接创建为链表)
# 1-2-0 在某个位置插入列表????? --> 我觉得可以实现(见03 多练)
# 2.删
# 2-1 删除头
# 2-2 删除尾
# 3.返回值(表示方法)
# 4.反转链表
# 5.查(查相应位置的节点)
# 6.改(更改目标节点的值)


class Node:   # 创建节点类
    def __init__(self, data, next1=None):
        self.data = data
        self.next = next1

    def __repr__(self):
        # return "node({})".format(self.data)
        return f"node({self.data})"


class LinkList:   # 创建链表类
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node   # 不管头空不空, 链表空不空, 插入头, 都要更新头/维护头

    def append(self, data):   # 插入尾 insert_tail  append , 列表方法中, 它也是默认在尾部追加一个元素
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)

    def insert(self, i, data):
        new_node = Node(data)      # 位置问题 链表的位置,从 1 开始
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

    def insert_list(self, object1: List):   # 尾部添加列表
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(object1[0])
            for i in object1[1:]:
                new_node = Node(i)
                temp.next.next = new_node
                temp = temp.next
        else:
            self.head = Node(object1[0])
            temp = self.head
            for i in object1[1:]:
                new_node = Node(i)
                temp.next = new_node
                temp = temp.next

    def delete_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        else:
            raise Exception("空链表")

    def delete_tail(self):
        if self.head:
            temp = self.head
            if temp.next is None:   # 只有头
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None   # 下下个为空了, 那么下一个就是尾, 删除即可
        else:
            return "空链表"

    def reverse(self):
        prev = None   # 设置一个虚拟的尾, 在头前
        current = self.head
        while current:
            next_node = current.next   # 先告诉右边的节点
            current.next = prev   # 转向
            prev = current   # 集体右移,左边先动,带动右边动
            current = next_node
        self.head = prev   # 维护头(属性)

    def __getitem__(self, index):   # 查  (__函数名__/__函数名: 私有函数)
        current = self.head

        if current is None:
            raise Exception("This is an empty linked list!")   # 错误提示,提示形式类似于报错,提示后代码不会继续执行(即便下面的代码没有问题)
            # return "空链表"

        for _ in range(1, index):   # 以下划线循环,因为此时只是需要一个循环次数,并非需要循环的这个变量(不同于i,下边会用到)
            if current.next is None:
                return "下标超出范围"
            current = current.next
        return current

    def get(self, index):   # 因为__name__是私有方法,一般只在类当中调用,所以需要另一个方法来调用它(供外部使用)
        return self.__getitem__(index)

    def __setitem__(self, index, data):
        current = self.head
        if current is None:
            # raise IndexError("The linked list is empty!") --> 错误提示
            return "空链表"
        for _ in range(1, index):
            if current.next is None:
                raise IndexError("Index out of range!")
                # return "下标越界"
            current = current.next
        current.data = data

    def set(self, index, data):
        return self.__setitem__(index, data)

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += "{}-->".format(current)
            current = current.next
        return string_repr + "END"


ll = LinkList()
ll.append(1)
ll.append(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert(3, 5)
ll.insert_list([6, 7, 8])
ll.delete_head()
ll.delete_tail()
ll.reverse()
# ll.get(2)    # 无返回结果??? 有返回值时打印了才能看到结果
print(ll.get(2))
ll.set(2, 9)
print(ll)
