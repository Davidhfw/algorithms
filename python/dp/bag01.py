# 01 背包问题
# 问题描述
# 问题描述为：给定一组物品，每种物品都有自己的重量和价格，在限定的总重量内，我们如何选择，才能使得物品的总价格最高。问题的名称来源于如何选择最合适的物品放置于给定背包中。
# 解决思路：动态规划，对每一件物品遍历背包容量，当背包可容纳值大于等于当前物品，与之前已放进去的物品所得价值进行对比，考虑是否需要置换。
# 动态规划转移方程如下:
#             0 if i = 0 or w = 0
# c[i,w] =    c[i-1,w]   if wi > w
#             max(vi + c[i-1, w-wi], c[i-1, w]),  if i > 0 and wi<= w
def bag01(n, c, w, v):
    """
        测试数据：
        n = 6  物品的数量，
        c = 10 书包能承受的重量，
        w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
        v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 初始化状态
    value = [[0 for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, c+1):
            if j >= w[i-1]:
                value[i][j] = max(value[i-1][j], value[i-1][j-w[i-1]] + v[i-1])
            else:
                value[i][j] = value[i - 1][j]

    return value[n][c]


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    print(bag01(n, c, w, v))
