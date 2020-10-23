from typing import List
# 26 有序数组去重   # 快指针走得快,去查找非重复值,好供慢指针所在重复值替换(因为有序数组,所以重复值挨在一起)
# class Solution1:
#
#     def remove_duplicated(self, nums: List[int]) -> int:
#         slow = 0
#         fast = 1  # 快指针在查找不重复的元素
#         while fast < len(nums):
#             if nums[slow] != nums[fast]:
#                 slow += 1
#                 nums[slow] = nums[fast]
#             fast += 1
#         return slow + 1
#
# s = Solution1()
# print(s.remove_duplicated([1,1,2,2,3,4]))

# if nums[fast] != nums[slow]:
#     slow += 1
#     nums[slow] = nums[fast]
#     fast += 1
# else:/elif:
#     fast += 1

# 283 移动零  # 快指针走得快,去查找非零值,好供慢指针所在位置的0替换
# class Solution2:
#     def move_zeroes(self, nums: List[int]) -> List[int]:
#         fast = 0  # 快指针在查找不为0的元素
#         slow = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]  # 该步操作使得当前几个元素非零时,原位替换(即不变化),以及零元素被替换掉(慢指针会停在零的位置)
#                 slow += 1
#                 fast += 1
#         for i in range(slow, len(nums)):
#             nums[i] = 0
#         return nums
#
#         # 有局限性
#         # n = len(set(nums))  # n = 2
#         # i = 0
#         # while i < n - 1:  # i = 0 循环1次
#         #     if nums[i] == 0:
#         #         nums[i: len(nums) - 1] = nums[i + 1:]
#         #         nums[-1] = 0
#         #         continue
#         #     else:
#         #         i += 1
#         # return nums
#
# s = Solution2()
# print(s.move_zeroes([1,0,0,1]))

# 27 去除指定元素
# class Solution3:
#     def remove_element(self, nums: List[int], value: int) -> int:
#         fast = 0
#         slow = 0
#         while fast < len(nums):
#             if nums[fast] == value:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
#         return slow
#
# s = Solution3()
# print(s.remove_element([3,2,3,2,2], 3))

# 80 删除排序数组的重复值(允许重复两次)
# class Solution4:
#     def remove_duplicates(self, nums: List[int]) -> int:
#         fast = 1
#         slow = 0
#         count = 1
#         while fast < len(nums):
#             if nums[fast] == nums[slow]:
#                 count += 1
#                 if count == 2:
#                     slow += 1
#                     nums[slow] = nums[fast]
#                 fast += 1
#             else:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 count = 1
#                 fast += 1
#         return slow + 1, nums
#
# s = Solution4()
# print(s.remove_duplicates([1,1,1,2,2,3,4]))
# # 尝试一下乱序什么情况

# 21 合并两个有序链表    递归???
# 1->2->3  1->3->4     -->  1->1->2->3->3->4


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"node({self.data})"
#
#
# class Solution5:
#     def merge_two_lists(self, list1, list2):
#         # prev1 = None
#         # prev2 = None
#         if list1.head:
#             if list2.head:
#                 curr1 = list1.head
#                 curr2 = list2.head
#                 while curr1:
#                     while curr2:
#                         if curr2.data >= curr1.data:
#                             curr2.next = curr1.next
#                             curr1.next = curr2
#                             list2.head = list2.head.next
#                         else:
#                             curr1.next = curr2.next
#                             curr2.next = curr1
#                         curr2 = curr2.next
#                     curr1 = curr1.next
#             else:
#                 current = list1.head
#                 string_repr = ""
#                 while current:
#                     string_repr += "{}-->".format(current)
#                     current = current.next
#                 return string_repr + "END"
#         else:
#             if list2.head:
#                 current = list2.head
#                 string_repr = ""
#                 while current:
#                     string_repr += "{}-->".format(current)
#                     current = current.next
#                 return string_repr + "END"
#             else:
#                 raise Exception("两个空链表")

# 24 两两交换链表中的节点
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f"node({self.data})"
#
#
# class Solution6:
#     def swap_pairs(self, head):
#         if head:
#             current = head
#             i = 0
#             while current and current.next:
#                 i += 1
#                 temp = current.next
#                 current.next = current.next.next
#                 temp.next = current
#                 # head1.next = temp  # 需要一个虚拟节点来连接交换后的两个节点,否则1连接不上4
#                 current = current.next
#                 if i == 1:
#                     head = temp
#                 # head1 = temp
#             temp1 = head
#             string_repr = ""
#             while temp1:
#                 string_repr += "{}-->".format(temp1)
#                 temp1 = temp1.next
#             return string_repr + "END"
#         else:
#             raise Exception("空链表")
#
# if __name__ == '__main__':
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#
#     s = Solution6()
#     print(s.swap_pairs(node1))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return "node({})".format(self.data)
#
#
# def swap_pairs(head: Node):   # 成对交换
#     dummy = Node(0)
#     dummy.next = head
#     current = dummy
#     while current.next and current.next.next:
#         # 指针上岗
#         fast = current.next.next
#         slow = current.next
#         # 交换位置
#         current.next = fast
#         slow.next = fast.next
#         fast.next = slow
#         # 节点后移
#         current = current.next.next
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
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     node5 = Node(5)
#     node6 = Node(6)
#     node7 = Node(7)
#
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#     node4.next = node5
#     node5.next = node6
#     node6.next = node7
#
#     print(swap_pairs(node1))

# 21 合并两个有序链表(归并排序)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)



def merge_two_lists(h1: Node, h2: Node):
    dummy = Node(0)
    current = dummy
    while h1 and h2:
        if h1.data <= h2.data:
            current.next = h1
            h1 = h1.next
        else:
            current.next = h2
            h2 = h2.next
        current = current.next

        if h1 is None:
            current.next = h2
        elif h2 is None:
            current.next = h1

    head = dummy.next
    curr = head
    string_repr = ""
    while curr:
        string_repr += "{}-->".format(curr)
        curr = curr.next
    return string_repr + "END"

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(3)
    node4 = Node(7)
    node5 = Node(1)
    node6 = Node(4)
    node7 = Node(5)
    node8 = Node(8)
    node9 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = None

    print(merge_two_lists(node1, node5))