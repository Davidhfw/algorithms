class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_largest_num(root, k):
    res = []

    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        else:
            return
    helper(root)
    return res[-k]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(kth_largest_num(root, 1))
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.left.left.left = TreeNode(1)
    print(kth_largest_num(root1, 3))
