# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。

# 解题思路
# 使用二分发查找数组，可能会找到一个有序的数组，如果没有，可以继续二分，最终一定可以找到一个有序数组，
class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # [left, mid]连续递增
            elif nums[left] <= nums[mid]:
                # target位于左侧区间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 否则去右侧区间查找
                else:
                    left = mid + 1
            # (mid, right]连续递增
            else:
                # target位于右侧,在右侧区间查找
                if nums[mid] <= target < nums[right]:
                    left = mid + 1
                # 否则去左侧区间查找
                else:
                    right = mid - 1
        return left if nums[left] == target else -1


if __name__ == '__main__':
    target = 0
    nums = [3, 4, 5, 6, 9, 0, 1, 2]
    result = Solution().search(nums, target)
    print(result)

