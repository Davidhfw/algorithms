def dicesProbability(n):
    dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
    for i in range(1, 7):
        dp[1][i] = 1
    for i in range(2, n + 1):
        for j in range(i, i * 6 + 1):
            for k in range(1, 7):
                if j >= k + 1:
                    dp[i][j] += dp[i-1][j-k]
    res = []
    for i in range(n, n * 6 + 1):
        res.append(dp[n][i] * 1.0 / 6 ** n)
    return res


if __name__ == '__main__':
    n = 9
    print(dicesProbability(2))
