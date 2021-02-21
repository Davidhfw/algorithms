import functools


def singleNumbers(nums):
    ret = functools.reduce(lambda x, y: x ^ y, nums)
    div = 1
    while div & ret == 0:
        div <<= 1
    a, b = 0, 0
    for n in nums:
        if n & div:
            a ^= n
            print(f'first group nums is {n}')
        else:
            b ^= n
            print(f'second group nums is {n}')
    return [a, b]


if __name__ == '__main__':
    nums = [4, 4, 5, 6, 8, 8, 9, 9, 0, 0]
    print(singleNumbers(nums))
