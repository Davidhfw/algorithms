# 题目描述: 二叉树的后序遍历
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
    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal1(self, root):
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res
    # 迭代法
    # 用栈迭代，
    #
    # 处理完根节点后，按照先右节点，最后左节点的顺序入栈。
    #
    # 这样总体的处理顺序就是中 - 左 - 右。
    def postorderTraversal2(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur_node = stack.pop()

            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

            res.append(cur_node.val)
        return res[::-1]


L = TreeNode(1)
L.left = None
L.right = TreeNode(2)
L.right.left = TreeNode(3)

print(Solution().postorderTraversal2(L))
