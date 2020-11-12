import heapq
from heapq import heapify, heappush, heapreplace, nsmallest, nlargest

class KthSmallest(object):
    def __init__(self, k, arr):
        self.k = k
        self.pool = nsmallest(k, arr)
        self.pool = [-x for x in self.pool]
        heapify(self.pool)

    def add(self, ele):
        ele = -ele
        if len(self.pool) < self.k:
            heappush(self.pool, ele)
        else:
            if self.pool[0] < ele:
                heapreplace(self.pool, ele)
        return -self.pool[0]


if __name__ == '__main__':
    arr = [1, 3, 8, 0, 4, 99, 47]
    result = KthSmallest(3, arr).add(9)
    print(result)