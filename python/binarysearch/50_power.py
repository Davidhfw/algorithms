# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
class Solution(object):
    def myPow(self, x, n):
        # 解法1：使用递归法，将问题的规模可以依次缩小为原来的一半，进行求解，注意n为负数和奇数的情况
        if not n:
            return 1
        if n < 0:
            return self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n/2)

    def myPow_1(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow


if __name__ == '__main__':
    n = 50
    x = 2
    res = Solution().myPow(x, n)
    res1 = Solution().myPow_1(x, n)
    print(res1)
    print(res)