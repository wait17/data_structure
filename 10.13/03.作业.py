from typing import List
# 15 合并两个有序数组


# def merge_two_array(nums1: List[int], m: int, nums2: List[int], n: int):
#     i = m - 1
#     j = n - 1
#     k = m + n - 1
#     while i >= 0 and j >= 0:
#         if nums1[i] >= nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#     # while i >= 0:
#     #     nums1[k] = nums1[i]
#     #     i -= 1
#     #     k -= 1
#     while j >= 0:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1
#
#
# print(merge_two_array([1, 2, 5, 6], 4, [2, 3, 4], 3))

# 反转数组
# def reverse(nums: List[int]):
#     left = 0
#     right = len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1
#     return nums
#
#
# print(reverse([1, 2, 3, 4, 5, 6, 7]))

# 数组的二分查找
# def dinary_search(nums: List[int], val: int):
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         if nums[left] == val:
#             return left
#         elif nums[right] == val:
#             return right
#         else:
#             mid = (left + right) // 2
#             if val < nums[mid]:
#                 right = mid
#             elif val > nums[mid]:
#                 left = mid
#             else:
#                 return mid
#
#
# print(dinary_search([1, 3, 4, 5, 6, 7, 8, 9], 3))

# 递归版
def
