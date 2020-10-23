# __init__.py作用
# 1 当一个文件夹中包含了__init__.py文件,python就会把这个文件夹当做一个package,从而能在其他文件夹中调用这个文件夹中的其他py文件(即init文件最大的作用是区别该文件夹是package还是纯粹的目录)
# 2 定义__all__用来模糊导入
# # python中的模块和包有两种导入方式,精确导入和模糊导入
# # 精确导入
# # from typing import List / import typing.List
# # 模糊导入(模糊导入中的 * 中的模块是由__all__来定义的)
# # from typing import *
# 3 可以编写Python代码--模块(但是不建议在__init__.py中写python模块, 可以在包中再创建另外的模块来写, 尽量保证__init__.py简单）

# 5 最长回文子串


def longest_palindrome(s):
    if len(s) <= 1 or s == s[::-1]:
        return s
    max_len = 1
    result = s[0]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                max_len = len(s[i:j+1])
                result = s[i:j+1]
    return max_len, result


# print(longest_palindrome("qqabqaap"))   # 有点问题,只能找到最后的回文子串


def longest_palindrome2(s):
    if len(s) <= 1 or s == s[::-1]:
        return s
    max_len = 1
    result = s[0]
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > max_len:   # 也不行???
                max_len = len(s[i:j+1])
                result = s[i:j+1]
    return max_len, result


# print(longest_palindrome2("abbbcccdeffe"))


# 中心延展法
def longest_palindrome_true(s: str) -> str:
    length = len(s)
    if length < 2:
        return s
    max_len = 1
    result = s[0]
    for i in range(length - 1):
        odd = center_spread(s, i, i)
        even = center_spread(s, i, i + 1)
        max_str = odd if len(odd) > len(even) else even
        if len(max_str) > max_len:
            max_len = len(max_str)
            result = max_str
    return result


def center_spread(s, left, right):
    length = len(s)
    i = left
    j = right
    while i >= 0 and j < length:
        if s[i] == s[j]:
            i -= 1
            j += 1
        else:
            break
    return s[i + 1: j]


if __name__ == '__main__':
    s = "abcbcbaefgaabbbaag"
    print(longest_palindrome_true(s))


from randomList import random_list
# 75 颜色分类
# 包含红色(0),白色(1),蓝色(2)三种元素n个元素的数组,使得相同颜色的元素排列在一起,并且按照红白蓝的顺序排列


def sort_colors(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


# print(sort_colors(random_list(10, 2)))


def colors_sort(nums):
    start, end = 0, len(nums) - 1
    i = 0
    while start <= end:
        if nums[i] == 0:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[end] = nums[end], nums[i]
            end -= 1
        else:
            i += 1
    return nums


# 求最大公约数(辗转相除法 + 更相减损术)  --> 更相减损术与移位相结合
def get_greatest_common_divisor(x, y):
    # big = max(x, y)
    # small = min(x, y)
    # if big % small == 0:
    #     return small
    # return get_greatest_common_divisor(small, big - small)

    big = max(x, y)
    small = min(x, y)
    d_value = big - small
    divisor = 1
    while small != d_value:
        if big % 2 == 0 and small % 2 == 0:   # 都偶
            big = big >> 1
            small = small >> 1
            divisor = divisor << 1
        elif big % 2 == 0 and small % 2 != 0:   # 大偶小奇
            big = big >> 1
            if big < small:
                big, small = small, big
        elif big % 2 != 0 and small % 2 == 0:   # 大奇小偶
            small = small >> 1
        else:   # 都偶
            big = max(small, d_value)
            small = min(small, d_value)
        d_value = big - small
    return d_value * divisor


# print(get_greatest_common_divisor(27, 18))
