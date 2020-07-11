# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#


class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_ele = matrix[mid // n][mid % n]
            if target == mid_ele:
                return True
            elif target < mid_ele:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [11, 13, 19, 22],
              [25, 44, 68, 99]]
    target = 11
    res = Solution().searchMatrix(matrix, target)
    print(res)