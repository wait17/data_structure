# 计数排序开始结尾有没有限制???
# def bucket_sort(nums):
#     length = len(nums)
#     big = max(nums)
#     small = min(nums)
#     ran = (big - small) / (length - 1)
#     res = [[None]] * length   # 不可行, 无法添加元素
#     res[1].append(1)
#     return res
#     # for val in nums:
#     #     if (val - small) / ran <
#
#
# print(bucket_sort([1, 2, 3, 4]))


def bucket_sort(nums):
    max_value = max(nums)
    min_value = min(nums)
    differ = max_value - min_value

    # 初始化桶
    bucket_num = len(nums)   # 桶的个数
    bucket_list = []   # 桶空间
    for _ in range(bucket_num):
        bucket_list.append([])

    # 将元素逐个放入桶中
    for val in nums:
        num = int((val - min_value) * (bucket_num - 1) / differ)   # 归一法(x - min)/(max - min)
        bucket = bucket_list[num]
        bucket.append(val)

    # 桶内部排序
    for i in range(bucket_num):
        bucket_list[i].sort()

    # 遍历输出
    result = []
    for j in range(bucket_num):
        for val in bucket_list[j]:
            result.append(val)

    return result


print(bucket_sort([4.5, 0.84, 0.5, 3.25, 2.18]))
