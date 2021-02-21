class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    if p.val < root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


def lowestCommonAncestor2(root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        
