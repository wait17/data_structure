def count_sort(nums):
    big = max(nums)
    small = min(nums)
    # res = []
    result = []
    # for i in range(0, big - small + 1):
    #     res.append(0)
    res = [0] * (big - small + 1)
    # return res
    for val in nums:
        res[val - small] += 1
    # return res
    for j in range(small, big + 1):
        # print(j)
        while res[j - small] != 0:
            result.append(j)
            res[j - small] -= 1
    return result


nums = [9, 3, 5, 4, 9, 1, 2, 7, 8, 1, 3, 6, 5, 3, 4, 0, 10, 9, 7, 9]
print(count_sort(nums))
