def isStraight(nums):
    repeat = set()
    max_v, min_v = 0, 14
    for num in nums:
        if num == 0:
            continue
        max_v = max(max_v, num)
        min_v = min(min_v, num)
        if num in repeat:
            return False
        repeat.add(num)
    return max_v - min_v < 5


if __name__ == '__main__':
     nums = [0, 0, 1, 4, 9]
     print(isStraight(nums))
