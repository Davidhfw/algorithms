def num_sum(nums, target):
    if not nums:
        return []
    if len(nums) < 2:
        return []
    hash_set = set()
    for i in range(len(nums)):
        if target - nums[i] in hash_set:
            return [nums[i], target - nums[i]]
        hash_set.add(nums[i])
    return []


if __name__ == '__main__':
    nums = [2, 7, 8, 9]
    target = 9
    print(num_sum(nums, target))
