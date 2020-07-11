# 题目描述
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

# 解题思路
# 维护一个最大值,每次去比较target值与最大值的差与当前值与target值的差的值, 取最小的值去更新当前值,
# 与15题类似,只不顾偶只需要一次遍历即可,剩下的两个值分别取前一个值的下一个元素和最后的元素即可, 两者组件逼近.


def threeSumClosest(nums, target):
    # 判断异常情况
    if not nums or len(nums) < 3:
        return None
    n = len(nums)
    # 对数组进行排序,方便后续两边逼近处理
    nums = sorted(nums)
    # 设置比较的最大值为正无穷大
    res = float('inf')
    for i in range(n):
        # 对于重复元素, 直接跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 左右逼近
        left = i + 1
        right = n - 1
        while left < right:
            cur_sum = nums[left] + nums[i] + nums[right]
            # 如果三数之和刚好等于目标值,此时与target距离最近的值就是目标值
            if cur_sum == target:
                return cur_sum
            # 判断与目标值的距离,将目前最小的距离值赋值给res,实现res的实时更新
            if abs(cur_sum - target) < abs(res - target):
                res = cur_sum
            # 当前值小于目标值, 左区间向右移
            if cur_sum - target < 0:
                left += 1
            # 当前值大于目标值, 右指针向左移
            if cur_sum - target > 0:
                right -= 1
    return res


nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))