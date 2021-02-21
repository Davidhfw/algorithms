def missingNumber(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = i + (j - i) // 2
        if nums[m] == m:
            i = m + 1
        else:
            j = m - 1
    return i


if __name__ == '__main__':
    nums = [0, 1, 3]
    nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    print(missingNumber(nums))
    print(missingNumber(nums1))
