# 快排思想: 确定一个中心,小于中心的放左边,大于中心的放右边
# 快速排序: 时间复杂度 -> o(n log n)
# def swap(array, a, b):
#     array[a], array[b] = array[b], array[a]
#
#
# def partition(array, start, end):   # partition: 分区
#     pivot = array[start]   # pivot: 中心,轴枢
#     p = start + 1
#     q = end
#     while p <= q:
#         while p <= q and array[p] < pivot:
#             p += 1
#         while p <= q and array[q] >= pivot:
#             q -= 1
#         if p < q:
#             swap(array, q, p)
#
#     swap(array, q, start)
#     return q
#
#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     mid = partition(array, start, end)
#     quick_sort(array, start, mid - 1)
#     quick_sort(array, mid + 1, end)
#     return array


# print(quick_sort([4, 3, 8, 7, 5, 6, 1, 2], 0, 7))


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(array, start, end):
    pivot = array[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and array[p] < pivot:
            p += 1
        while p <= q and array[q] >= pivot:
            q -= 1
        if p < q:
            swap(array, p, q)

    swap(array, q, start)
    return q


def quick_sort(array, start, end):
    if start >= end:
        return
    mid = partition(array, start, end)
    quick_sort(array, start, mid - 1)
    quick_sort(array, mid + 1, end)
    return array


print(quick_sort([4, 3, 8, 7, 5, 6, 1, 2], 0, 7))
