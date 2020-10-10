"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
解题思路：　
方法三、动态规划：自下而上 [通过]
算法：

我们采用自下而上的方式进行思考。仍定义 F(i)F(i) 为组成金额 ii 所需最少的硬币数量，假设在计算 F(i)F(i) 之前，我们已经计算出 F(0)-F(i-1)F(0)−F(i−1) 的答案。 则 F(i)F(i) 对应的转移方程应为

F(i)=\min_{j=0 \ldots n-1}{F(i -c_j)} + 1
F(i)=
j=0…n−1
min
​
 F(i−c
j
​
 )+1

其中 c_jc
j
​
  代表的是第 jj 枚硬币的面值，即我们枚举最后一枚硬币面额是 c_jc
j
​
 ，那么需要从 i-c_ji−c
j
​
  这个金额的状态 F(i-c_j)F(i−c
j
​
 ) 转移过来，再算上枚举的这枚硬币数量 11 的贡献，由于要硬币数量最少，所以 F(i)F(i) 为前面能转移过来的状态的最小值加上枚举的硬币数量 11 。

例子1：假设


coins = [1, 2, 5], amount = 11
则，当 i==0i==0 时无法用硬币组成，为 0 。当 i<0i<0 时，忽略 F(i)F(i)

F(i)	最小硬币数量
F(0)	0 //金额为0不能由硬币组成
F(1)	1 //F(1)=min(F(1-1),F(1-2),F(1-5))+1=1F(1)=min(F(1−1),F(1−2),F(1−5))+1=1
F(2)	1 //F(2)=min(F(2-1),F(2-2),F(2-5))+1=1F(2)=min(F(2−1),F(2−2),F(2−5))+1=1
F(3)	2 //F(3)=min(F(3-1),F(3-2),F(3-5))+1=2F(3)=min(F(3−1),F(3−2),F(3−5))+1=2
F(4)	2 //F(4)=min(F(4-1),F(4-2),F(4-5))+1=2F(4)=min(F(4−1),F(4−2),F(4−5))+1=2
...	...
F(11)	3 //F(11)=min(F(11-1),F(11-2),F(11-5))+1=3F(11)=min(F(11−1),F(11−2),F(11−5))+1=3
我们可以看到问题的答案是通过子问题的最优解得到的。

例子2：假设


coins = [1, 2, 3], amount = 6


在上图中，可以看到：

\begin{aligned} F(3) &= \min({F(3- c_1), F(3-c_2), F(3-c_3)}) + 1 \\ &= \min({F(3- 1), F(3-2), F(3-3)}) + 1 \\ &= \min({F(2), F(1), F(0)}) + 1 \\ &= \min({1, 1, 0}) + 1 \\ &= 1 \end{aligned}
F(3)
​

=min(F(3−c
1
​
 ),F(3−c
2
​
 ),F(3−c
3
​
 ))+1
=min(F(3−1),F(3−2),F(3−3))+1
=min(F(2),F(1),F(0))+1
=min(1,1,0)+1
=1
​
"""


class Solution(object):
    def coin_change(self, coins, amounts):
        dp = [float("inf") for _ in range(amounts + 1)]
        dp[0] = 0
        for i in range(1, amounts + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1

if __name__ == '__main__':
    coins = [1, 2, 5]
    amounts = 23333
    res = Solution().coin_change(coins, amounts)
    print(res)
