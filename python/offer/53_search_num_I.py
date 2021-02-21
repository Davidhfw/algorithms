def search(nums, target):
    # 搜索右边界right
    i, j = 0, len(nums) - 1
    while i <= j:
        m = i + (j - i) // 2
        if nums[m] <= target:
            i = m + 1
        else:
            j = m - 1
    right = i
    if j >= 0 and nums[j] != target:
        return 0
    # 搜索左边界
    print(f'i is {i}')
    print(f'j is {j}')
    i = 0
    while i <= j:
        m = i + (j - i) // 2
        if nums[m] < target:
            i = m + 1
        else:
            j = m - 1
    left = j
    return right - left - 1


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search(nums, target))
