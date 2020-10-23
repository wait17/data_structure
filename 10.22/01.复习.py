# 归并排序
def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left = nums[:mid]
    right = nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


# print(merge_sort([3, 8, 9, 5, 6, 1, 3, 2]))


def merge2(left, right):
    l_len = len(left)
    r_len = len(right)
    i = 0
    j = 0
    result = []
    while i < l_len and j < r_len:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort2(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge2(merge_sort2(left), merge_sort2(right))


# print(merge_sort2([3, 8, 9, 5, 6, 1, 3, 2]))


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(array, start, end):
    qivot = array[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and array[p] < qivot:
            p += 1
        while p <= q and array[q] >= qivot:
            q -= 1
        if p < q:
            swap(array, p, q)
    swap(array, start, q)
    return q


def quick_sort(array, start, end):
    if start >= end:
        return
    mid = partition(array, start, end)
    quick_sort(array, start, mid - 1)
    quick_sort(array, mid + 1, end)
    return array


# print(quick_sort([3, 8, 9, 5, 6, 1, 3, 2], 0, 7))


# 快慢指针
# 有序数组去重
def remove_duplicated(nums):
    slow = 0
    fast = 1
    # while fast < len(nums):
    #     if nums[fast] == nums[slow]:
    #         fast += 1
    #     else:
    #         slow += 1
    #         nums[fast], nums[slow] = nums[slow], nums[fast]
    #         fast += 1
    # return nums[: slow + 1]

    # 简化代码
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            # nums[slow], nums[fast] = nums[fast], nums[slow]
            nums[slow] = nums[fast]   # 因为只要去重后的数组, 其他元素不必理会
        fast += 1
    return nums[: slow + 1]


# print(remove_duplicated([1, 1, 2, 2, 2, 3, 5, 5, 6]))


# 移动零
def remove_zero(nums):   # 把零提前
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] != 0:
            fast += 1
        else:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
            fast += 1
    return nums


print(remove_zero([1, 0, 0, 1, 4, 0, 5, 0, 0]))
