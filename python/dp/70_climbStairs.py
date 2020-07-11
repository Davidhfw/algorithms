class Solution:
    def climbStairs(self, n):
        dp = [0 for _ in range(n+1)]
        print(dp)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


print(Solution().climbStairs(100))