from heapq import heapreplace, heapify, heappush, nlargest

class KthLargest(object):
    def __init__(self, k, arr):
        self.k = k
        self.pool = nlargest(self.k, arr)
        heapify(self.pool)

    def add(self, ele):
        if len(self.pool) < self.k:
            heappush(self.pool, ele)
        else:
            if self.pool[0] < ele:
                heapreplace(self.pool, ele)
        return self.pool[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 9]
    result = KthLargest(3, nums).add(5)
    print(result)