from typing import Optional
# 快慢指针判断是否存在环

# 竖着同时选取怎么选?   右击-->column selection mode 勾选上(-->使用后再勾选掉)
# if name = main???
# __name__是当前模块名，当模块被直接运行时模块名为_main_，也就是当前的模块，当模块被导入时，模块名就不是__main__，即代码将不会执行
# 自动换行???
# 归纳,枚举 --> 入环点
# 快慢指针推导公式
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)

def is_circle(head: Node):
    fast = head
    slow = head
    while fast and fast.next:  # 用慢指针可能会发生NoneType has no attribute of next(空类型没有next属性)错误
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def detectCirclePoint(head: Optional[Node] = None):
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
    return slow

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
    node7.next = node4

    print(is_circle(node1))
    print(detectCirclePoint(node1))