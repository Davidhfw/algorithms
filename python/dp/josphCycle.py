# -*- coding:utf-8 -*-

class Solution(object):
    def lastRemaining(self, n, m):
        if not n or not m:
            return -1
        lst = [i for i in range(n)]
        i = 0
        while len(lst) > 1:
            i = (m - 1 + i) % len(lst) # 递推公式
            lst.pop(i)
        return lst[0]

m = 3
n = 10
print(Solution().lastRemaining(n, m))