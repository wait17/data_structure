# 优先队列中的每个元素都有各自的优先级,优先级最高的元素最先得到服务
# 优先级相同的元素按照其在优先队列中的顺序得到服务,优先队列往往用堆来实现
# 靠堆实现存在最大最小优先级的队列


class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, data):
        self.array.append(data)
        self.size += 1
        self.heapify_up()

    def dequeue(self):
        if self.size <= 0:
            raise Exception("空队列")
        remove_data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_data

    def heapify_up(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) >> 1
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) >> 1   # 或者(child_index - 1) // 2 除二后向下取整(默认向下取整)
        self.array[child_index] = temp

    def heapify_down(self):
        total_index = self.size - 1
        index = 0
        while True:
            max_value_index = index
            if 2 * index + 1 <= total_index and self.array[2 * index + 1] > self.array[max_value_index]:
                max_value_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.array[2 * index + 2] > self.array[max_value_index]:
                max_value_index = 2 * index + 2
            if max_value_index == index:
                break
            self.array[index], self.array[max_value_index] = self.array[max_value_index], self.array[index]
            index = max_value_index


if __name__ == '__main__':
    q = PriorityQueue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(7)
    q.enqueue(6)
    q.enqueue(2)
    q.dequeue()
    # print(q.size)
    print(q.array)
