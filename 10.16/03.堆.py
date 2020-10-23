# 堆
# 二叉堆
# 最大堆, 最小堆
# 二进制 十进制 八进制 十六进制
# 右移一位(除二)  左移一位(乘二)


class Heap:
    def __init__(self):
        # 初始化一个空堆,使用数组来存放堆元素,节省存储空间
        self.data_list = []

    def get_parent_index(self, index):
        # 取到下标为index的节点的父节点的下标
        if index <= 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1   # 返回的是下标
            # 数组储存二叉树,会按照层序顺序把节点放到相应位置
            # 如果某个节点的孩子空缺,数组对应位置也空缺(即相应下标还是被占用,只不过是被空节点占用)
            #

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent and self.data_list[index] > self.data_list[parent]:
            self.swap(index, parent)
            index = parent
            parent = self.get_parent_index(index)

    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        max_value_index = index
        total_index = len(self.data_list) - 1
        while True:
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[max_value_index]:
                max_value_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[max_value_index]:
                max_value_index = 2 * index + 2
            if max_value_index == index:
                break
            self.swap(index, max_value_index)
            index = max_value_index


if __name__ == '__main__':
    heap = Heap()
    heap.insert(10)
    heap.insert(9)
    heap.insert(8)
    heap.insert(11)
    heap.insert(15)
    print(heap)

