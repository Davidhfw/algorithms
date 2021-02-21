import collections


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_tree_dfs(root):
    if not root:
        return 0
    return 1 + max(depth_tree_dfs(root.left), depth_tree_dfs(root.right))


def depth_tree_bfs(root):
    if not root:
        return 0
    queue, res = collections.deque(), []
    queue.append(root)
    while queue:
        cur = []
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            cur.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        res.append(cur)
    return len(res)



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(depth_tree_dfs(root))
    print(depth_tree_bfs(root))
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.left.left.left = TreeNode(1)
    print(depth_tree_dfs(root1))
    print(depth_tree_bfs(root1))
