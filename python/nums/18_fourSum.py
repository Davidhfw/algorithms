# # 题目描述
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# 解题思路:
# 1 对原数组进行排序, 处理输入数组为None或者长度小于4或者排序后前四个数的和大于target,则直接返回空列表, 这里排序建议使用sorted函数,该函数不会直接在原数组上进行排序
# 而sort()函数会直接排序原数组
# 2 对前两个数分别进行两轮遍历,对于第三和第四个数使用两个左右指针逼近的办法去解决
# 3 注意遇到数组中的重复元素,需要跳过处理
# 4 本题要去输出结果不重复,应该率先想到使用set去重

# 使用set数据结构
def fourSumWithSet(nums, target):
    if not nums or len(nums) < 4:
        return []
    new_nums = sorted(nums)
    if sum(new_nums[:4]) > target:
        return []
    n = len(new_nums)
    res = set()

    for first in range(n-2):
        for second in range(first + 1, n-1):
            third = second + 1
            fourth = n - 1
            while third < fourth:
                cur_sum = new_nums[first] + new_nums[second] + new_nums[third] + new_nums[fourth]
                if cur_sum == target and (new_nums[first], new_nums[second], new_nums[third], new_nums[fourth]) not in res:
                    res.add((new_nums[first], new_nums[second], new_nums[third], new_nums[fourth]))
                elif cur_sum < target:
                    third += 1
                else:
                    fourth -= 1
    return map(list, res)

# 使用列表数据结构,需要主动判重
def fourSumWithList(nums, target):
    if not nums or len(nums) < 4:
        return []
    new_nums = sorted(nums)
    if sum(new_nums[:4]) > target:
        return []
    n = len(new_nums)
    res = []

    for first in range(n-3):
        if first > 0 and new_nums[first] == nums[first - 1]:
            continue
        for second in range(first + 1, n-2):
            if second > first + 1 and new_nums[second] == new_nums[second - 1]:
                continue
            third = second + 1
            fourth = n - 1
            while third < fourth:
                cur_sum = new_nums[first] + new_nums[second] + new_nums[third] + new_nums[fourth]
                if cur_sum == target:
                    res.append([new_nums[first], new_nums[second], new_nums[third], new_nums[fourth]])
                    while third < fourth and new_nums[third] == new_nums[third + 1]:
                        third += 1
                    while third < fourth and new_nums[fourth] == new_nums[fourth - 1]:
                        fourth -= 1
                    third += 1
                    fourth -= 1
                elif cur_sum < target:
                    third += 1
                else:
                    fourth -= 1
    return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
res = fourSumWithSet(nums, target)
for i in res:
    print(i)