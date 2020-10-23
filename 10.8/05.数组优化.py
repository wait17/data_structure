# 自动添加函数???
class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        if index < 0:
            raise IndexError("索引越界")
        if index >= len(self.array) or self.size >= len(self.array): # 后半部分不理解  size从什么开始
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1): # 代码逻辑问题, 并画图加深理解
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self,index):
        if index < 0 or index > self.size:  # 虽然理论上可以隔空插入,但是不符合常理
            raise IndexError("数组越界")
        for i in range(index,self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i])

if __name__ == '__main__':
    a = Array(5)
    a.insert(0, 1)
    a.insert(1,2)
    a.insert(2,3)
    a.insert(3,4)
    a.remove(1)
    print(a.array)
    print(a.size)