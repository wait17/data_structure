from randomList import random_list
# 冒泡排序

s_nums = random_list(5, 10)


def bubble_sort(nums):
    count = 0
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                count += 1
                print("第%s次排序结果: %s" % (count, nums))
    return nums


# 优化
def bubble_sort_y(nums):
    for i in range(len(nums) - 1):
        flag = True
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:
            break
    return nums


# print(bubble_sort(s_nums))
print(bubble_sort_y([5, 2, 3, 4, 1]))


# 选择排序
# 内层循环负责找到最小值索引
# 外层循环控制排序轮数
def selection_sort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


# print(selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
