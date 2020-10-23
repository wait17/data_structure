# 快速排序
def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


def partition(nums, start, end):
    qivot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < qivot:
            p += 1
        while p <= q and nums[q] >= qivot:
            q -= 1
        if p < q:
            swap(nums, p, q)
    swap(nums, start, q)
    return q


def quick_sort(nums, start, end):
    if start >= end:
        return
    mid = partition(nums, start, end)
    quick_sort(nums, start, mid - 1)
    quick_sort(nums, mid + 1, end)
    return nums


# print(quick_sort([1, 5, 6, 8, 7, 3, 4, 2], 0, 7))


# 单指针实现快排
def partition2(nums, start, end):
    pivot = nums[start]
    mark = start
    for i in range(start + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[i], nums[mark] = nums[mark], nums[i]
    nums[start] = nums[mark]
    nums[mark] = pivot
    return mark


def quick_sort2(nums, start, end):
    if start >= end:
        return
    mid = partition2(nums, start, end)
    quick_sort2(nums, start, mid - 1)
    quick_sort2(nums, mid + 1, end)
    return nums


# print(quick_sort2([5, 6, 1, 8, 7, 3, 4, 2], 0, 7))


# 计数排序
def count_sort(nums):
    big = max(nums)
    small = min(nums)
    result = []
    res = [0] * (big - small + 1)
    for val in nums:
        res[val - small] += 1
    # return res
    for i in range(small, big + 1):
        while res[i - small] != 0:
            result.append(i)
            res[i - small] -= 1
    return result


print(count_sort([9, 3, 8, 2, 9, 6, 3, 5, 1, 8, 7, 6, 2, 3]))


# 字典树
class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return "{}".format(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if node is None:
                return False
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if node is None:
                return False
        return True


# if __name__ == '__main__':
    # trie = Trie()
    # trie.insert("some")
    # print(trie.root.data)
    # print(trie.search("some"))
    # print(trie.starts_with("so"))
