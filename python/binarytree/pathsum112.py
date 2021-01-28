"""
题目描述：　给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

解题思路：
１　广度优先遍历
首先我们可以想到使用广度优先搜索的方式，记录从根节点到当前节点的路径和，以防止重复计算。

这样我们使用两个队列，分别存储将要遍历的节点，以及根节点到这些节点的路径和即可。
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    @staticmethod
    def has_path_sum(root, target):
        # 异常情况处理
        if root is None:
            return False
        # 将根节点及其值加入到双端队列中
        que_node = deque([root])
        que_node_val = deque([root.val])
        # 判断当前节点是否为子节点
        while que_node:
            now = que_node.popleft()
            temp = que_node_val.popleft()
            # 如果已经到了子节点，比较从根节点到当前节点的值的和是否与给定值相等
            if not now.left and not now.right:
                if temp == target:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_node_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_node_val.append(now.right.val + temp)
        return False

    # 递归
    def has_sum_path_recur(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return target == root.val
        return self.has_sum_path_recur(root.left, target - root.val) or self.has_sum_path_recur(root.right, target - root.val)

    # 回溯法
    def path_sum_dfs(self, root, target):
        res, path = [], []
        def recur(root, target):
            # 如果节点为空，直接返回
            if not root: return
            # 将根节点值加入列表
            path.append(root.val)
            # 减去该点的值
            target -= root.val
            # 判断和为target并且已经到达叶子节点
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            # 递归遍历左右子树
            recur(root.left, target)
            recur(root.right, target)
            path.pop()
        recur(root, target)
        return res


if __name__ == '__main__':
    l = TreeNode(5)
    l.left = TreeNode(4)
    l.right = TreeNode(8)
    l.left.left = TreeNode(11)
    l.left.left.left = TreeNode(7)
    l.left.left.right = TreeNode(2)
    l.right.left = TreeNode(13)
    l.right.right = TreeNode(4)
    l.right.right.right = TreeNode(1)
    res = Solution().has_path_sum(l, 23)
    print(res)
    res1 = Solution().has_sum_path_recur(l, 22)
    print(res1)


