"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
进阶：
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
你能在线性时间复杂度内解决此题吗？
解题思路：

１　将数组中的前ｋ个元素依次加入到滑动窗口中，选出最大值，并将下表之前的值从窗口中删除，将最大值下标及之后的位于窗口中的值的下表存入到ｗｉｎｄｏｗ中，　
依次循环，
"""


def maxSlidingWindow(nums, k):
    if nums is None:
        return []
    elif len(nums) == 0:
        return []

    window, res = [], []
    for index, val in enumerate(nums):
        # 保证滑动窗口中的元素个数为k个,超过k个后,最左边的元素要被移除出窗口中
        if index >= k and window[0] <= index-k:
            window.pop(0)

        # 如果窗口中最后一个元素小于当前遍历的值,则把窗口中这个元素之前的下标值全部删除
        while window and nums[window[-1]] <= val:
            window.pop()
        window.append(index)

        if index >= k-1:
            res.append(nums[window[0]])
    return res


if __name__ == "__main__":
    nums = [1, 3, -5, 0, 2, 9, -2]
    k = 3
    ret = maxSlidingWindow(nums, k)
    print(ret)



