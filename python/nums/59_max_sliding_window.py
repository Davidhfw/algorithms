"""
滑动窗口的最大值， 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
解题思路：使用一个双端队列保存k大小窗口中最大值，先依次将k个元素保存进队列中，并且只保存最大值。然后从k到数组长度，
"""

import collections

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    deque = collections.deque()
    for i in range(k):
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
    res = [deque[0]]
    for i in range(k, len(nums)):
        # 保持窗口大小始终为k
        if deque[0] == nums[i-k]:
            deque.popleft()
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
        res.append(deque[0])
    return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(max_sliding_window(nums, k))

