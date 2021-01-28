class Solution:
    def findRepeatNumber(self, nums):
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 0
            else:
                return i
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))
