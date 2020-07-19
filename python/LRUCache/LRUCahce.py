import collections
class LRUCache:
    def __init__(self, capacity):
        self.dct = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dct:
            return -1
        v = self.dct.pop(key)
        self.dct[key] = v
        return v

    def put(self, key, value):
        if key in self.dct:
            self.dct.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dct.popitem(last=False)
        self.dct[key] = value