from pprint import pformat
# 两数之和
# def two_sum(nums, target):
#     for i in range(len(nums) - 1):
#         n = target - nums[i]
#         if n in nums[i + 1:]:
#             j = nums.index(n)
#             return i, j
#
#
# print(two_sum([3, 2, 4], 6))


# def two_sum(nums, target):
#     start = 0
#     end = len(nums) - 1
#
#     while start < end:
#         sum_two = nums[start] + nums[end]
#         if sum_two == target:
#             print(start, end)
#             start += 1
#             end -= 1
#         else:
#             if sum_two < target:
#                 start += 1
#             else:
#                 end -= 1
#
#
# two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 8)


# def two_sum(nums, target):
#     dict = {}
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         if temp in dict:
#             return [i, nums[temp]]
#         else:
#             dict[nums[i]] = i

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def __repr__(self):
#         return f"{self.data}"
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         node = Node(data)
#         if self.root is None:
#             self.root = node
#         else:
#             temp = [self.root]
#             while True:
#                 pop_node = temp.pop(0)
#                 if pop_node.left is None:
#                     pop_node.left = node
#                     return
#                 elif pop_node.right is None:
#                     pop_node.right = node
#                     return
#                 else:
#                     temp.append(pop_node.left)
#                     temp.append(pop_node.right)
#
#     def get_parent(self, val):
#         if self.root.data == val:
#             raise Exception("根节点无父节点")
#         temp = [self.root]
#         while temp:
#             pop_node = temp.pop(0)
#             if pop_node.left:
#                 if pop_node.left.data == val:
#                     return pop_node
#                 temp.append(pop_node.left)
#             if pop_node.right:
#                 if pop_node.right.data == val:
#                     return pop_node
#         return None
#
#
# t = Tree()
# t.insert(1)
# t.insert(2)
# t.insert(3)
# print(t.root.left)
# print(t.get_parent(2))


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({"%s" % (self.data) : (self.left, self.right)}, indent=1)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def __insert(self, data):
        node = Node(data)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                else:



