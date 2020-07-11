# 题目描述
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 说明:
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
# 解题思路: 1 递归与分治, 每次计算x*x, 计算n/2,将问题规模化小
class Solution:
    def myPow(self, x, n):
        if type(n) != int:
            raise AssertionError('bot ')
        # 处理n为负整数的情况
        if n < 0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            # 判断n是否为奇数
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

    def myPow_recur(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow_recur(x, -n)
        if n % 2:
            return x * self.myPow_recur(x, n-1)
        return self.myPow_recur(x*x, n / 2)

import time
t1_start = time.time()
print(Solution().myPow(2.5, 100))
t1_end = time.time()
print('t1 cost time is ', t1_end - t1_start)
t2_start = time.time()
print(Solution().myPow_recur(2.5, 100))
t2_end = time.time()
print('t2 cost time is ', t2_end - t2_start)