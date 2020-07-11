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
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal1(self, root):
        res = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        helper(root)
        return res
    # 迭代法

    def inorderTraversal2(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            # 将根节点和左子树压入栈依次压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 弹出左子树的值,并将值加入到res中
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res


L = TreeNode(1)
L.left = None
L.right = TreeNode(2)
L.right.left = TreeNode(3)

print(Solution().inorderTraversal2(L))
