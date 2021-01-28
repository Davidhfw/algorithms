class Solution:
    def numWays(self, n: int) -> int:
        if n < 0:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

if __name__ == '__main__':
    print(Solution().numWays(9))