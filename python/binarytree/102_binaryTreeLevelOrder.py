# 题目描述
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 解题思路: 1 广度优先遍历: 将每一层的节点加入到队列中, 遍历队列,将值加入列表中
# 解题思路2: 深度优先遍历, 将每一次的结果加入到列表中,并记录列表层数,实现对树的层次遍历
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def level_order_bfs(self, root):
        if not root:
            return []
        # 创建一个双端队列,用来保存树中每一层的节点
        queue = collections.deque()
        res = []
        # 先将root节点加入到队列中
        queue.append(root)
        # visited = set()

        # 只要队列不为空,就一直循环
        while queue:
            cur_level_len = len(queue)
            cur_res = []
            for _ in range(cur_level_len):
                cur_node = queue.popleft()
                cur_res.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(cur_res)
        return res

    def level_order_dfs(self, root):
        if not root: return []
        self.res = []
        self._dfs(root, 0)
        return self.res

    def _dfs(self, node, level):
        if not node: return
        if len(self.res) < level + 1:
            self.res.append([])
        self.res[level].append(node.val)
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)

if __name__ == '__main__':
    root = TreeNode(9)
    root.left = TreeNode(11)
    root.right = TreeNode(9)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(0)
    res = Solution().level_order_bfs(root)
    print(res)
