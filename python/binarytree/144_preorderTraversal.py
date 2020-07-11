# 题目描述: 二叉树的中序遍历
# 解题思路1: 递归解决
# 递归终止条件:节点为空,返回
# 子问题分割: 分别去遍历左右递归的子节点
# 树节点构造

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal1(self, root):
        res = []
        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return res
    # 迭代法
    # 用栈迭代，
    #
    # 处理完根节点后，按照先右节点，最后左节点的顺序入栈。
    #
    # 这样总体的处理顺序就是中 - 左 - 右。
    def preorderTraversal2(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            res.append(cur_node.val)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return res


L = TreeNode(1)
L.left = None
L.right = TreeNode(2)
L.right.left = TreeNode(3)

print(Solution().preorderTraversal2(L))
