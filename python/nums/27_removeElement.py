class Solution:
    def removeElement(self, nums, val):
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                nums[i] = None
        count = 0
        for i in range(length):
            if nums[i] is not None:
                count += 1
        return count

    def removeElement_1(self, nums, val):
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        i = 0
        for j in range(length):
            if nums[j] != val:
                nums[i] = nums[j]
        return i

x = dict()


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 2
    print(Solution().removeElement_1(nums, val))

