# 题目描述
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。

# 解题思路1: a + b + c = 0 , 也就是a = -(b + c) , 也就是用一个字典存储这些值, 这里需要注意的是, 不允许重复,所以最终的结果以set保存, 达到自动去重的目的

def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        # 遇到数组中的重复元素,直接跳过
        if i >= 1 and nums[i] == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1  # 这里的1只是将-v-x放入到字典中,没有什么其他的意义
            else:
                res.add((v, -v-x, x))

    return map(list, res)


def threeSum1(nums):
    res = []
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    n = len(nums)
    for i in range(len(nums) -2):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif three_sum > 0:
                right -= 1
            else:
                left += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum1(nums))






