class Solution(object):
    def sortArray(self, nums):
        self.nums = nums
        if not nums or len(nums) <= 1:
            return nums
        n = len(nums)
        return self.quick(0, n-1)

    def quick(self, start, end):
        if start >= end:
            return
        pivot, left, right = start, start, end
        while left < right:
            while left < right and self.nums[right] > self.nums[pivot]:
                right -= 1
            while left < right and self.nums[left] <= self.nums[pivot]:
                left += 1
            self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
        self.nums[pivot], self.nums[left] = self.nums[left], self.nums[pivot]
        self.quick(start, left - 1)
        self.quick(left + 1, end)
        return self.nums


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 0, 0, 0, 2, 3, 4, 5, 3, 99]
    print(Solution().sortArray(nums))



