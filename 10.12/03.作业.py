# 1 两数之和 --元素重复情况 --时间、空间复杂度 --逻辑结构(结合图分析)
# class Solution:
#     def two_sum(self, nums, target):   # 暴力拆解: 时间复杂度太大 o(n^2)
#         i = 0
#         result = []
#         while i < len(nums) - 1:
#             j = 1
#             while j < len(nums):
#                 if i != j and nums[i] + nums[j] == target:
#                     result.append(i)
#                     result.append(j)
#                     return result
#                 j += 1
#             i += 1

# #   合适解答
#     def two_sum(self, nums, target):
#         for i in range(len(nums)-1):
#             a = target - nums[i]
#             if a in nums[i + 1:]:
#                 j = nums.index(a, i + 1, len(nums))
#                 if i != j:
#                     return i, j

#     def two_sum(self, nums, target):   # 对撞指针(相向而行)   # 时间复杂度: o(nlogn)
#         nums.sort()   # 本解针对有序列表
#
#         start = 0
#         end = len(nums) - 1
#         while start < end:
#             sum_two = nums[start] + nums[end]
#             if sum_two == target:
#                 print(start, end)
#                 start += 1
#                 end -= 1
#             else:
#                 if sum_two > target:
#                     end -= 1
#                 else:
#                     start += 1
#
#     def two_sum(self, nums, target):   # 时间复杂度: o(n)
#         sum_dict = {}
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if temp in sum_dict:
#                 return [i, nums[temp]]
#             else:
#                 sum_dict[nums[i]] = i
#
#     def two_sum(self, nums, target):   # 时间复杂度: o(n^2)
#         for i in range(len(nums) - 1):
#             for j in nums[i + 1:]:
#                 if nums[i] + j == target:
#                     return True
#         return False

# s = Solution()
# s.two_sum([3, 3, 4], 6)


# 15 三数之和   ???情况较多,较复杂
# class Solution:
#     def three_sum(self, nums):
#         result = [0]
#         if 0 not in nums:
#             pass
#         else:
#             for i in range(len(nums)):
#                 a = 0 - nums[i]
#                 if a in nums[i + 1:]:
#                     j = nums.index(a, i + 1, len(nums))
#                     if i != j:
#                         result.append(nums[i])
#                         result.append(nums[j])
#                         break
#         return result
#
#
# s = Solution()
# print(s.three_sum([1, 0, 2, 5, -5, 8, -5, 5]))

# from typing import List
#
#
# def two_sum(nums: List, target):
#     nums2 = nums.copy()
#     nums.sort()
#
#
#     right= len(nums) - 1
#     left=0
#     while left < right:
#         sum_two = nums[right] + nums[left]
#         if sum_two<target:
#             left+=1
#         if sum_two>target:
#             right-=1
#         if sum_two==target:
#             a = nums2.index(nums[left])
#             b = nums2.index(nums[right])
#             print (nums[left],nums[right],a,b)
#             right-=1
#             left+=1

# two_sum([5,4,3,3,2,1],7)
# def three_sum(sums, target):
#     for i in range(len(sums) - 2):
#         for j in range(i + 1, len(sums) - 1):
#             temp = target - sums[i] - sums[j]
#             if temp in sums:
#                 k = sums.index(temp)
#                 print(i, j, k)
#
#
# three_sum([-1, 2, 5, -2, 8, 9, 3], 6)


def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                # result.append([nums[i], nums[left], nums[right]])
                result += [[nums[i], nums[left], nums[right]]]   # 更优, 不使用高级函数
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result


print(three_sum([5, 3, 4, 0, -1, -5, -8, -3, -3, 1]))


def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                # result.append([nums[i], nums[left], nums[right]])
                result += [[nums[i], nums[left], nums[right]]]   # 更优, 不使用高级函数
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


print(three_sum([5, 3, 4, 0, -1, -5, -8, -3, -3, 1]))
