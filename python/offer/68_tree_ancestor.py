
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if not root or p.val == root.val or q.val == root.val:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left:
        return right
    if not right:
        return left
    return root

