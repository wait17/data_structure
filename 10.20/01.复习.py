# 二分查找
def dinary_search(nums, data):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == data:
            return left
        elif nums[right] == data:
            return right
        else:
            mid = (left + right) // 2
            if nums[mid] < data:
                left = mid
            elif nums[mid] > data:
                right = mid
            else:
                return mid


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 6, 7, 8, 9, 11]
    # print(dinary_search(nums, 5))   # 该法遇到数组中不存在的值时死循环


def dinary_search2(nums, data):
    if data not in nums:
        return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        # if nums[left] == data:
        #     return left
        # elif nums[right] == data:
        #     return right
        # else:
        mid = (left + right) // 2
        if nums[mid] > data:
            right = mid-1
        elif nums[mid] < data:
            left = mid+1
        else:
            return mid


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(dinary_search2(nums, 9))
