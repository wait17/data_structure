def longest_palindrome(s):
    if len(s) <= 1 or s == s[::-1]:
        return s
    max_len = 1
    num = s[0]

    for i in range(len(s) - 1):
        # if max_len > len(s[i + 1:]):  # 待求解长度没有超过最大长度，结束
        #     break
        for j in range(i + max_len, len(s)):  # 从长度为最大长度+1的子串开始求解
            if s[i:j + 1] == s[i:j + 1][::-1] and j - i + 1 > max_len:
                max_len = j - i + 1
                num = s[i:j + 1]
    return num


# 求最大公约数(辗转相除法 + 更相减损术)  --> 更相减损术与移位相结合
def get_greatest_common_divisor(x, y):
    big = max(x, y)
    small = min(x, y)
    if big % small == 0:
        return small
    return get_greatest_common_divisor(small, big - small)


# print(get_greatest_common_divisor(5, 25))
#
# print(longest_palindrome("helolqq"))

# for i in range(0):   # 取不到数据
#     print("===")
#     print(i)

# nums = [2, 1, 4, 3, 5]
# # nums.sort()
# nums.sort(reverse=True)
# print(nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums.pop(0))
