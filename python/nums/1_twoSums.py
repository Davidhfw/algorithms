# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 解题思路：
# 使用一个字典来保存下表， 然后枚举遍历数组， 只要数组出现target - x的元素，那么就将target - x 和x的下标返回，否则就将x的下标存储在nums中，注意数组nums异常情况
def twoSum(nums, target):
    if len(nums) < 2 or not nums:
        return []

    hash_map = {}
    for index, val in enumerate(nums):
        if target - val in hash_map:
            return [index, hash_map[target - val]]
        hash_map[val] = index

