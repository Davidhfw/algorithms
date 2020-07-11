
class Trie(object):
    """
    实现trie字典树
    """
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    # 向字典树中插入一个单词
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    # 从字典树中搜索单词
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    # 在字典树中查询前缀
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('beijing')
    # obj.insert('hainan')
    # res_2 = obj.search('beijig')
    # res_3 = obj.startsWith('beij')
    # print(res_2)
    # print(res_3)
