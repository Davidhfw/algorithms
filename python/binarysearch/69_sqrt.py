# 题目描述
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去
#
# 解题思想, 二分查找, 逐渐逼近
class Solution:
    def mySqrt(self, x):
        # 特殊情况处理
        if x == 0 or x == 1:
            return x

        # 此时x大于1
        left = 1
        right = x
        res = 0
        while left <= right:
            # mid = left + ((right - left) >> 1)
            mid = left + (right - left) // 2
            if mid == x / mid:
                return int(mid)
            elif mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1
                res = mid
        return int(res)

print(Solution().mySqrt(18))
