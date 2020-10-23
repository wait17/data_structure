class Node:
    def __init__(self, data, next1=None):
        # next1=None 可不写(写next参数,则必须给定默认值,否则次次需要传入值),不写的话,需要在下面(self.next)设置默认值
        self.data = data   # 前一个data是属性,后一个data是传入的值(即上方的data)
        self.next = next1

    def __repr__(self):
        # return "node({})".format(self.data)
        return f"node({self.data})"   # 把一个对象表示成字符串形式


# n = Node(1)
# print(n)

# 查/索引
# 增  插入
# insert方法: 五种情况
# 1 下标越界
# 2 空链表
# 3 从头插入
# 4 从尾插入
# 5 中间插入
# 删
# 改
# 反转链表
# 返回值(表示)

class LinkList:
    def __init__(self):
        # 初始化链表(定义属性)
        # 多了尾属性和长度属性,操作更方便
        self.head = None   # 维护头结点
        self.tail = None   # 维护尾结点
        self.size = 0      # 维护链表长度

    def get(self, index):   # 下标是下标, 长度(size)是长度, 下标通常比长度小一
        current = self.head
        if current is None:
            raise Exception("空链表")
        elif index >= self.size:
            raise IndexError("Index out of range!")
        for _ in range(index):  # 从1开始,对应正常思维的下标,index为3, 取到第三个节点; 若从0开始,则是代码思维的下标,index为3, 取到第四个节点  --> 代码思维
            # 此时从0开始(联系size属性),对应下边代码
            # 循环index - 1次
            current = current.next
        return current

    def insert(self, index, data):
        new_node = Node(data)

        if index < 0 or index > self.size:  # 去掉index > self.size, 则下边下标大于长度时可以插入新节点(尾部插入)
            raise IndexError("下标越界")
        else:
            if self.size == 0:  # 空链表
                self.head = new_node
                self.tail = new_node
            elif index == 0:   # 从头插入
                new_node.next = self.head
                self.head = new_node
            elif index == self.size:   # 从尾插入  条件改为index >= self.size, 则下标超出的也能插入到尾部
                self.tail.next = new_node
                self.tail = new_node
            else:   # 中间插入
                prev = self.get(index - 1)
                new_node.next = prev.next   # 链表思想: 先安排后事, 再放手一搏
                prev.next = new_node
            self.size += 1   # 插入节点后, 维护长度属性

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")
        if self.size == 0:
            raise Exception("The linked list is empty!")
        else:
            if index == 0:   # 删除头
                remove_node = self.head
                self.head = self.head.next
                remove_node.next = None
            elif index == self.size - 1:   # 删除尾
                prev = self.get(index - 1)
                remove_node = self.tail
                prev.next = None
                self.tail = prev
            else:
                prev = self.get(index - 1)
                remove_node = prev.next
                prev.next = prev.next.next
                remove_node.next = None
            self.size -= 1
            return remove_node   # 根据python标准, 一般删除函数的返回值是被删除的元素

    def reverse(self):
        pre = None
        current = self.head
        while current:   # 反转链表三大步四小步
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
        self.tail = self.head
        self.head = pre

    def set(self, index, data):
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:   # 把一个对象表示成字符串形式, 但形成方式特殊(遍历链表后拼接)
            string_repr += "{}-->".format(current)   # 箭头只是可视化表示,内部不是靠线或者箭头连接,靠前一个储存下一个的内存地址联系
            current = current.next
        return string_repr + "END"


ll = LinkList()
ll.insert(0, 1)
ll.insert(0, 2)
ll.insert(2, 3)
ll.insert(2, 4)
ll.remove(2)
print(ll.get(2))
ll.set(1, 5)
ll.reverse()
print(ll)
