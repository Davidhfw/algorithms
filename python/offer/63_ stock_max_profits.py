
# 显示当前 python 程序占用的内存大小
import os

import psutil as psutil


def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def max_profit(prices):
    # dp定义：dp[i]代表第i天卖出股票后获得的最大利润
    show_memory_info('initial max_profit')
    n = len(prices)
    dp = [0 for _ in range(n)]
    for i in range(1, n):
        dp[i] = max(dp[i-1], prices[i] - min(prices[0:i]))
    show_memory_info("after max_profit")
    return dp[n-1]


def max_profit_upgrade(prices):
    show_memory_info('initial max_profit improve')
    cost, profit = float("+inf"), 0
    for price in prices:
        # 记录最低价格
        cost = min(cost, price)
        profit = max(profit, price - cost)
    show_memory_info('initial max_profit improve finished')
    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4, 8, 9, 10, 11, 23, 19]
    #print(max_profit_upgrade(prices))
    print(max_profit(prices))
    # prices1 = [7, 6, 4, 3, 1]
    # print(max_profit(prices1))
    # prices1 = [7, 6, 4, 3, 1]
    # print(max_profit_upgrade(prices1))
