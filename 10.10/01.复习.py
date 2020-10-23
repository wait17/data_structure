# 怎么自动导入???
# 移动零
# class Solution1:
#     def move_zeroes(self, nums):
#         fast = 0
#         slow = 0
#         while fast < len(nums):
#             if nums[fast] == 0:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
#         for i in range(slow, len(nums)):
#             nums[i] = 0
#         return nums
#
# s = Solution1()
# print(s.move_zeroes([1,0,1,0]))

# 有序数组去重
# class Solution2:
#     def remove(self, nums):
#         fast = 1
#         slow = 0
#         while fast < len(nums):
#             if nums[slow] == nums[fast]:
#                 fast += 1
#             else:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 fast += 1
#         return slow + 1, nums
#
# s = Solution2()
# print(s.remove([1,1,2,3,3,4]))

# 有序数组去重(最多允许重复两次)
# class Solution3:
#     def remove(self, nums):
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
# s = Solution3()
# print(s.remove([1,1,1,2,2,3,4]))

# 去除指定元素
# class Solution4:
#     def remove_value(self, nums, value):
#         fast = 0
#         slow = 0
#         while fast < len(nums):
#             if nums[fast] == value:
#                 fast += 1
#             else:
#                 nums[slow] = nums[fast]
#                 slow += 1
#                 fast += 1
#         return slow, nums
#
# s = Solution4()
# print(s.remove_value([1,2,3,1,2,3,4], 2))

# 数组实现栈
# class Stack:  # stackofarray
#     def __init__(self):
#         self.stack = []
#         self.size = 0
#
#     def __str__(self):
#         return str(self.stack)
#
#     def push(self, value):
#         self.stack.append(value)
#         self.size += 1
#
#     def pop(self):   # 先做判断
#         self.stack.pop()
#         self.size -= 1
#
#     def peek(self):   # 先做判断
#         if self.size == 0:
#             raise Exception("空栈")
#         else:
#             return self.stack[-1]  # 试一下不写else
#
#     def is_empty(self):
#         pass
#
#     def size1(self):
#         return self.size
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()
# print(s.stack, s.size)

# 链表实现栈
class Node:
    def __init__(self, data):
        self.data = data
        self.
class Stack:
    def __init__(self):
        pass