'''
题目描述： 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
例如:
给定二叉树: [3,9,20,null,null,15,7],
'''
import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_bfs(root):
    if not root: return []
    result = []
    queue = collections.deque()

    queue.append(root)

    # visited = set()

    while queue:
        level_size = len(queue)
        current_level_res = []
        # 增加for循环将每层节点全部遍历完
        for _ in range(level_size):
            node = queue.popleft()
            current_level_res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(current_level_res)

    return result


class Solution:
    '''
    1 采用算法， 广度优先算法或深度优先算法
    2 将每一层的节点加入队列中，循环输出每个节点值，并加入到当前层的结果中，然后将下一层节点加入到队列中，直到所有节点均访问完毕， 队列为空，结束循环
    3 注意对空树的状态检测
    '''

    def level_order_dfs(self, root):
        """
        深度优先算法思想：按照深度优先算法将二叉树的每一个分支遍历一遍，然后记录每个节点的层数，将相同节点层数的节点值合并，最后输出结果
        对每一层构造出[], 加入到结果中备用
        """

        if not root: return []
        self.result = []
        self._dfs(root, 0)
        return self.result


    def _dfs(self, node, level):
        if not node: return

        # 将[]加入到每层结果中，即使当前层还没有输出结果
        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


if __name__ == '__main__':
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    result = level_order_bfs(t)
    print('bfs result is ', result)
    result_dfs = Solution().level_order_dfs(t)
    print('dfs result is ', result_dfs)






