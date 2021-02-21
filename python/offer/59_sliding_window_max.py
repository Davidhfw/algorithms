import collections


def max_sliding_window(nums, k):
    # 输入异常情况判断
    if not nums or len(nums) < k:
        return []
    # 构造最开始拥有k个元素的窗口，使用队列存储这些元素
    res = []
    deque = collections.deque()
    for i in range(k):
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
    # 窗口刚形成，直接将队列首位元素加入到返回列表中
    res = [deque[0]]
    # 接下来滑动窗口
    for i in range(k, len(nums)):
        # 滑动窗口范围不包括deque[0]元素，需要将该元素从队列中删除
        if deque[0] == nums[i - k]:
            deque.popleft()
        # 如果队列中最后一个元素小于nums[i]，则将队列中的元素全部删除
        while deque and deque[-1] < nums[i]:
            deque.pop()
        deque.append(nums[i])
        res.append(deque[0])
    return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 4
    print(max_sliding_window(nums, k))
