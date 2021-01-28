class Solution:
    def fib(self, n):
        res = [0 for _ in range(n+1)]
        res[0] = 0
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

if __name__ == '__main__':
    print(Solution().fib(5))