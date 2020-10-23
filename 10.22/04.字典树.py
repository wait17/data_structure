# 字典树: 又称单词查找树, Trie树, 前缀树, 是一种树形结构, 是一种哈希树的变种
# 典型应用是用于统计, 排序和保存大量的字符串(但不仅限于字符串), 所以经常被搜索引擎系统用于文本词频统计
# 优点是: 利用字符串的公共前缀来减少查询时间, 最大限度的减少无谓的字符串比较, 查询效率比哈希树高

# 三个基本性质: 根节点不包含字符, 除根节点外每一个节点都只包含一个字符; 从根节点到某一节点, 路径上经过的字符连接起来, 为该节点对应的字符串; 每个节点的所有子节点包含的字符都不相同


class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return "{}".format(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()   # Trie树的根是一个空字典

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()   # 此时的char是一个key, 其value是一个空字典
            node = node.data[char]   # node下移, 移动到char的value的位置,即空字典的位置
            # 注意: node.data 是空字典, 而不是node是空字典
        node.is_word = True   # 单词完全传入后, 定义is_word属性为True(只传入一半不算单词)

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word   # 如果只查询单词的一半, 那么拿到的结果为False, 因为只有在单词的末尾才会更改属性为True

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("something")
    print(trie.root.data)
    # print(trie.search("some"))
    # print(trie.search("something"))
    print(trie.starts_with("so"))
