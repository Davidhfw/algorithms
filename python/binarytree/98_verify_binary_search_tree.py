# 题目描述
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# 解题思路1: 对当前的树进行中序遍历, 查看遍历之后的结果是否为有序数组, 时间复杂度是ologn, 空间复杂度是on
# 解题思路2: 对当前树进行中序遍历, 每次使用前继节点与当前节点进行比较,如果当前节点大于前继节点, 则返回False
# 解题思路3: 递归遍历树的左右节点,找到这棵树中左子树的最大值及右子树的最小值, 并与当前根节点做比较, 只有左子树的最大值小于根节点, 右子树的最小值大于根节点, 才是二叉搜索树
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 未改进的中序遍历
    def isValidBSTInOrder(self, root):
        if not root:
            return []
        inorder = self.inorderTraversal(root)
        return inorder == list(sorted(set(inorder)))

    def inorderTraversal(self, node):
        if not node:
            return []
        return self.inorderTraversal(node.left) + [node.val] + self.inorderTraversal(node.right)

    # 改进后的中序遍历
    def isValidBSTInOrderUpgrade(self, root):
        if not root: return []
        self.prev = None
        return self.helper(root)

    def helper(self, node):
        if not node: return True
        if not self.helper(node.left): return False
        if self.prev and self.prev.val >= node.val: return False
        self.prev = None
        return self.helper(node.right)

    # 迭代法的中序遍历
    def isValidBSTWithIter(self, root):
        p = root
        stack = []
        pre = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if pre and pre.val >= p.val:
                return False
            pre = p
            p = p.right
        return True

    # 利用最大最小值
    def isValidBST(self, root):
        if not root: return True
        min_val = float('-inf')
        max_val = float('inf')
        return self.isBST(root, min_val, max_val)

    def isBST(self, node, min_val, max_val):
        if not node:
            return True
        if node.val >= max_val or node.val <= min_val:
            return False
        return self.isBST(node.left, min_val, max_val) and self.isBST(node.right, min_val, max_val)
    