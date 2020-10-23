# 未完成   +   单独实现反转方法
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "node({})".format(self.data)
#
#
# class LinkList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, index, data):
#         node = Node(data)
#         if self.head is None:
#             self.head = node
#
#     def reverse(self):
#         dummy = Node(0)
#         pre = dummy
#         current = self.head
#         while current:
#             temp = current.next
#             current.next = pre
#             pre = current
#             current = temp
#         self.head = pre


# 数组反转
def reverse_array(nums):
    length = len(nums)
    left = 0
    right = length - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


# nums = [1, 2, 3, 4, 5]
# print(reverse_array(nums))


# 两两交换链表中的节点
def swap_pairs(head: Node):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        fast = current.next.next
        slow = current.next
        slow.next = fast.next
        fast.next = slow
        current.next = fast

        current = current.next.next
    head = dummy.next
    current = head
    string_repr = ""
    while current:
        string_repr += "{}-->".format(current)
        current = current.next
    return string_repr + "END"


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    # print(swap_pairs(node1))


# 三数之和
# def three_sum(nums):
#     nums.sort()
#     length = len(nums)
#     result = []
#     if length < 3:
#         return -1
#     for i in range(length - 2):
#         while i > 0 and nums[i] == nums[i - 1]:
#             continue
#         left = i + 1
#         right = length - 1
#         while left < right:
#             sum_3 = nums[i] + nums[left] + nums[right]
#             if sum_3 < 0:
#                 left += 1
#             elif sum_3 > 0:
#                 right -= 1
#             else:
#                 # result += [nums[i], nums[left], nums[right]]
#                 result += [[nums[i], nums[left], nums[right]]]
#                 # result.append([nums[i], nums[left], nums[right]])
#                 left += 1
#                 right -= 1
#     return result
#
#
# print(three_sum([1, 0, 3, 5, -1, 6, 4, -3, -2]))


# 有效三角形
# def triangle(nums):
#     count = 0
#     nums.sort()
#     for val in nums:
#         if val <= 0:
#             nums.remove(val)
#     length = len(nums)
#     for i in range(length - 1, 1, -1):
#         left = 0
#         right = i - 1
#         if nums[left] + nums[right] > nums[i]:
#             for left in range(right):
#                 if nums[i] - nums[left] < nums[right]:
#                     count += 1
#                 else:
#                     right -= 1
#         else:
#             left += 1
#     return count
#
#
# print(triangle([2, 2, 3, 4]))

# 合并两个有序数组

# 合并两个有序链表
