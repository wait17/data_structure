def partition(array, start, end):
    pivot = array[start]
    mark = start
    for i in range(start + 1, end + 1):
        if array[i] < pivot:
            mark += 1
            array[i], array[mark] = array[mark], array[i]
    array[start] = array[mark]
    array[mark] = pivot
    return mark


def quick_sort(array, start, end):
    if start >= end:
        return
    mid = partition(array, start, end)
    quick_sort(array, start, mid - 1)
    quick_sort(array, mid + 1, end)
    return array


print(quick_sort([4, 7, 3, 5, 6, 2, 8, 1], 0, 7))
