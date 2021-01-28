# 给定一个二维矩阵，请顺时针打印矩阵元素
def revolve_matrix_clockwise(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    res = []
    left, right, top, bottom = 0, cols - 1, 0, rows - 1,
    while True:
        # 从左到右遍历
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        if top > bottom:
            break
        # 从上到下遍历
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if left > right:
            break
        # 从右到左遍历
        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
        bottom -= 1
        if top > bottom:
            break
        # 从下到上遍历
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        if left > right:
            break
    return res


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(revolve_matrix_clockwise(matrix))

