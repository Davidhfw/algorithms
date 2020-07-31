"""
题目描述：
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

＃１　深度优先搜索
将二维网格看成一个无向图，竖直或水平相邻的 1 之间有边相连。
为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 11，则以其为起始节点开始进行深度优先搜索。在深度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 00。
最终岛屿的数量就是我们进行深度优先搜索的次数。
"""
import collections
class Solution(object):
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)


    def numsIslands(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        nums_island = 0
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == '1':
                    nums_island += 1
                    self.dfs(grid, row, col)

        return nums_island

    # 广度优先搜索：同样地，我们也可以使用广度优先搜索代替深度优先搜索。
    #
    # 为了求出岛屿的数量，我们可以扫描整个二维网格。如果一个位置为 11，则将其加入队列，开始进行广度优先搜索。在广度优先搜索的过程中，每个搜索到的 11 都会被重新标记为 00。直到队列为空，搜索结束。
    #
    # 最终岛屿的数量就是我们进行广度优先搜索的次数。

    def numsIslandBfs(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        nums_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    nums_island += 1
                    grid[r][c] = '0'
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                                neighbors.append((x, y))
                                grid[x][y] = '0'

        return nums_island


if __name__ == '__main__':
    grid = [
                ['1','1','1','1','0'],
                ['1','1','0','1','0'],
                ['1','1','0','0','0'],
                ['0','0','0','0','0']
            ]
    grid1 = [
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
    # res = Solution().numsIslands(grid1)
    # print(res)
    res1 = Solution().numsIslandBfs(grid1)
    print(res1)

