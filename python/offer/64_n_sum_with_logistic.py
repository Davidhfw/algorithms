class Solution(object):
    def __init__(self):
        self.res = 0

    def sumNums(self, n):
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    sol = Solution()
    print(sol.sumNums(100))
