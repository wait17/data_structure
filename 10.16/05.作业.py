# 461 汉明距离
# 思路：做异或,计算1的个数


# def hanming_distance(a, b):
#     c = a ^ b
#     pass


# 477 汉明距离总和
# 思路：遍历做异或
# def total_hanming_distance(nums):
#     result = 0
#     for i in nums:
#         a = i ^ (i + 1)
#         b = pass
#         result += b
#     return b


# 求两个数的最大公约数
def divisor(x, y):   # 时间复杂度o(min(x, y)) 较麻烦
    if x < y:
        r = x
    else:
        r = y
    for i in range(1, r + 1):
        if x % i == 0 and y % i == 0:
            divisor = i
    return divisor


# 普通解法: 暴力枚举法(1)   时间复杂度: o(min(x,y))  --> o(min(x, y)/2)
def common_divisor(x, y):
    big = max(x, y)
    small = min(x, y)
    if big % small == 0:
        return small
    for i in range(small // 2, 0, -1):   # 因为要考虑最小数的约数, 一个数的约数(除本身外)最大是它的一半
        if small % i == 0 and big % i == 0:
            return i


# 辗转相除法(2): 两个正整数a, b(a>b),他们的最大公约数等于a除以b的余数c和b之间的最大公约数
# ??? 欧几里得算法
# 时间复杂度: 近似为o(log(max(x,y))), 但是取模运算性能较差
# 缺陷: 两个大数取模运算麻烦
def get_greatest_common_divisor(x, y):
    big = max(x, y)
    small = max(x, y)
    if big % small == 0:
        return small
    return get_greatest_common_divisor(small, big % small)


# 更相减损术(3): 两个正整数a, b(a>b),他们的最大公约数等于a-b的差c和b之间的最大公约数
# 时间复杂度: 避免了取模运算(取余运算), 但是算法性能不稳定, 最坏时间复杂度为o(max(x,y))
# 缺陷: 一大一小数取差次数多
def get_greatest_common_divisor2(x, y):
    if x - y == 0:
        return y
    big = max(x, y)
    small = min(x, y)
    return get_greatest_common_divisor2(big - small, small)


# 更相减损术与位移结合(辗转相除法)(4), 避免了取模运算, 并且算法性能稳定, 时间复杂度为o(log(max(x,y)))
# print(divisor(35, 70))
# print(common_divisor(4, 3))
print(get_greatest_common_divisor2(115, 65))
