# 导入列表模块
from typing import List


class Student:   # 创建类
    def __init__(self, name, sex, age):   # 属性(初始化方法)
        self.name = name                  # 前一个name是属性, 后一个name是传入的参数=上边的name
        self.sex = sex
        self.age = age
        self.parent = None                # 不传入参数的属性, 默认为空

    def study(self):   # 方法
        print("%s在学习" % self.name)

    def rest(self):   # 方法
        print("%s在休息" % self.name)


# s1 = Student("张三", "男", 22)   # 初始化对象, s1 是一个对象, 打印时拿到的是内存地址(除非有表示函数)
# print(s1)
# s1.study()
# s1.rest()


class Node:   # 创建节点类(node: 节点)
    def __init__(self, data, next1=None):
        self.data = data
        # 上边括号当中的next1=None, 意思是给next1(传入的参数)一个默认值,下边左侧的next是一个属性
        # 不传入next1时默认为空
        self.next = next1

    def __repr__(self):   # 表示/表达方法(represent: 代表,表现)
        # 不写表示方法打印时打印出对象,内存地址;写表示方法后直接打印出所设置打印内容
        # format: 字符串占位方法
        # return "node({})".format(self.data)
        return f"node({self.data})"
        # return "{}".format(self.data) --> 直接打印出节点的值


# n = Node(1000)
# print(n)


class LinkList:   # 创建链表类
    # 初始化对象(属性)
    def __init__(self):
        self.head = None   # 维护头

    # 头部增加
    def insert_head(self, data):
        new_node = Node(data)   # 增加一个节点的第一步都是先创建一个新的节点
        if self.head is not None:   # 头不空
            new_node.next = self.head
        self.head = new_node   # 重置头/维护头

    # 尾部增加
    def append(self, data):
        new_node = Node(data)
        if self.head is not None:
            temp = self.head   # 遍历链表, 移动temp遍历
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.insert_head(data)

    # 中间插入
    def insert(self, i, data):   # 第i个位置(不是下标  下标加一)插入data
        if self.head is None:   # 头空 --> 空链表
            self.insert_head(data)
        elif i == 1:   # 在第一个位置插入节点 --> 从头插入节点
            self.insert_head(data)
        else:
            temp = self.head   # 遍历到相应位置后插入
            j = 1
            pre = temp
            while j < i:   # 即从第一个位置,走 i - 1 步(循环i - 1次)
                pre = temp
                temp = temp.next
                j += 1
            new_node = Node(data)
            pre.next = new_node
            new_node.next = temp

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += "{} --> ".format(current)
            current = current.next
        return string_repr + "END"

# 实例化对象
# 先创建链表,才能执行插入操作(因为链表是个类,得先创建)
# l = LinkList()
# l.insert_head(1)
# l.insert_head(2)
# l.insert(2, 4)
# l.append(3)
# print(l)


class LinkList1:
    def __init__(self):
        self.head = None

    def insert_list(self, object1: List):  # object命名? 出问题是因为object是关键字, 所以稍微改一下
        self.head = Node(object1[0])   # 空链表插入列表
        temp = self.head
        for i in object1[1:]:
            new_node = Node(i)
            temp.next = new_node
            temp = temp.next

    def __repr__(self):
        current = self.head   # 遍历打印
        string_repr = ""
        while current:
            string_repr += "{}-->".format(current)
            current = current.next
        return string_repr + "END"

    def delete_head(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None   # 为了将旧头彻底断开
        else:
            raise Exception("空链表")

    def delete_tail(self):
        temp = self.head
        if self.head:
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            raise Exception("空链表")


l2 = LinkList1()
l2.insert_list([1, 2, 3, 4, 5, 6])
l2.delete_head()
l2.delete_tail()
print(l2)   # 最后一行,下边敲一个空行,就不会再报波浪线了
