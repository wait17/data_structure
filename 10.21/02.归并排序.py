# 归并排序: 时间复杂度 -> o(n log n)
def merge(left, right):
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))   # 底层代码显示: pop作用, 删除相应位置元素,默认删除最后一位, 返回值为弹出的元素
        else:
            result.append(left.pop(0))
    if left:
        result.extend(left)   # extend 可传入列表, 作用为将列表中元素依次加入result
    if right:
        result.extend(right)
    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left, right = nums[:mid:], nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


# print(merge_sort([8, 3, 2, 5, 9, 3, 6, 7]))


def merge1(left, right):
    l_len = len(left)
    r_len = len(right)
    result = []
    i = 0
    j = 0
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


def merge_sort1(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left, right = nums[:mid], nums[mid:]
    return merge1(merge_sort1(left), merge_sort1(right))

    
print(merge_sort([8, 3, 2, 5, 9, 3, 6, 7]))
