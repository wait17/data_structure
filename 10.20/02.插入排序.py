# 插入排序(扑克牌思维)
def insert_sort(nums):
    if len(nums) <= 1:
        return nums
    for right in range(1, len(nums)):
        target = nums[right]
        for left in range(right):
            if nums[left] > target:
                nums[left + 1:right + 1] = nums[left:right]
                nums[left] = target
                break
    return nums


# if __name__ == '__main__':
#     nums = [1, 8, 9, 5, 6, 2, 3]
#     print(insert_sort(nums))


# 链表 插入排序
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.insert_head(data)

    def __repr__(self):
        current = self.head
        strs = ""
        while current:
            strs += "{}-->".format(current)
            current = current.next
        return strs + "END"


def insert_sort_list(head: Node):   # 创建了一个新的链表
    dummy = Node(0)
    pre = dummy

    cur = head
    while cur:
        temp = cur.next
        while pre.next and pre.next.data < cur.data:
            pre = pre.next
        cur.next = pre.next
        pre.next = cur

        cur = temp
        pre = dummy
    return dummy.next


if __name__ == '__main__':
    # node1 = Node(8)
    # node2 = Node(7)
    # node3 = Node(9)
    # node4 = Node(5)
    # node5 = Node(3)
    # node6 = Node(6)
    # node7 = Node(1)
    #
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    # node6.next = node7
    # node7.next = None
    #
    # print(insert_sort_list(node1))

    ll = LinkList()
    ll.append(8)
    ll.append(7)
    ll.append(9)
    ll.append(5)
    ll.append(3)
    ll.append(6)
    ll.append(1)
    print(ll)
    print(insert_sort_list(ll.head))
    # print(ll.head)
