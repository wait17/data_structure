def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    sum_1 = 0
    len_1 = float("inf")
    if length < 1:
        return 0
    else:
        for i in range(length - 1):
            if nums[length - 1] >= s or nums[i] >= s:
                return 1
            start = i
            end = start + 1
            sum_1 = nums[start] + nums[end]
            while end < length and sum_1 < s:
                end += 1
                if end < length:
                    sum_1 += nums[end]
                if end == length - 1 and sum_1 < s:
                    return 0
            if sum_1 >= s and len(nums[start: end + 1]) < len_1:
                len_1 = len(nums[start: end + 1])
    return len_1


# print(minSubArrayLen(15, [1, 2, 3, 4, 25]))


def min_sub_array_len(s, nums):
    if not nums:
        return 0
    length = len(nums)
    sum_1 = 0
    result = float("inf")
    left = 0
    for right in range(length):
        sum_1 += nums[right]
        while sum_1 >= s:
            res = min(result, len(nums[left: right+1]))
            sum_1 -= nums[left]
            left += 1
    return res if res != result else 0


print(min_sub_array_len(15, [1, 2, 3, 4, 5]))


def min_sub_array_len2(s, nums):
    left, sum_s, res = 0, 0, float("inf")
    for right in range(len(nums)):
        sum_s += nums[right]
        while sum_s >= s:
            if right - left + 1 < res:
                res = right - left + 1
            sum_s -= nums[left]
            left += 1
    return res if res != float("inf") else 0


def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    length = len(nums)
    if length == 3:
        result = nums[0] + nums[1] + nums[2]
        return result

    nums.sort()
    result = 0  # 三数之和
    differ = float("inf")  # 差值 默认为正无穷
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            res = nums[i] + nums[left] + nums[right]
            dif = res - target
            if abs(dif) < differ:
                differ = abs(dif)
                result = res
            if res < target:
                left += 1
            elif res > target:
                right -= 1
            else:
                return target
    return result


# print(threeSumClosest([1, 5, 6, -3, -5], 7))


def three_sum_closest(nums, target):
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    pass

