import collections


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def balance_tree_judge(root):
    def recur(root):
        if not root:
            return 0
        left = recur(root.left)
        if left == -1:
            return -1
        right = recur(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1
    return recur(root) != -1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(balance_tree_judge(root))
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.left.left.left = TreeNode(1)
    print(balance_tree_judge(root1))
