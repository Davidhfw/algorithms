# 题目描述
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
# 解题思路1: 使用递归法递归遍历树
# 解题思路2: 记录p和q的查找路径,然后找到这两个路径中的相交节点


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowest_common_ancestor(self, root, p, q):
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        return root

    def lowest_common_ancestor_iter(self, root, p, q):
        import collections
        if not root:
            return None
        parent = {root: None}
        queue = collections.deque([root])
        while queue or p not in parent or q not in parent:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
        # find parent path
        path = set()
        while p:
            path.add(p)
            p = parent[p]
        while q not in path:
            q = parent[q]
        return q
