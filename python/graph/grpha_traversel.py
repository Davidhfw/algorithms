# 图的定义，使用邻接矩阵
class Graph:
    def __init__(self, val):
        self.val = val
        self.neighbors = None

# 图的广度优先遍历
# 1 利用队列实现
# 2 从源节点开始按照宽度进队列，然后弹出
# 3 每弹出一个节点，就把该节点所有没进过队列的邻接节点
# 4 直到队列变空

def bfs_graph(node):
    from collections import deque

    if not node:
        return
    # 节点队列
    queue = deque()
    # 保存已经访问过的节目
    visited = set()

    queue.append(node)
    visited.add(node)
    while queue:
        cur_node = queue.popleft()
        print(cur_node.val)
        for nxt in cur_node.neighbors:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

# 图的深度优先遍历（非递归）
# 1 利用栈实现
# 2 从源节点开始把节点按照深度放入栈中， 然后弹出
# 3 每弹出一个节点，把该节点的下一个还没入栈的邻接点进入栈
# 4 直到栈变空
def dfs_graph(node):
    if not node:
        return

    visited = set()
    stack = []
    stack.append(node)
    visited.add(node)
    print(node.val)
    while len(stack) > 0:
        cur = stack.pop()
        for nxt in cur.neighbors:
            if nxt not in visited:
                stack.append(cur)
                stack.append(nxt)
                visited.add(nxt)
                print(nxt.val)
                break
# 递归深度遍历
def dfs_graph_1(node, visited):
    if not node:
        return
    print(node.val)
    visited.add(node)
    for nxt in node.neighbors:
        if nxt not in visited:
            dfs_graph_1(nxt, visited)


if __name__ == '__main__':
    node5 = Graph(5)
    node4 = Graph(4)
    node3 = Graph(3)
    node2 = Graph(2)
    node1 = Graph(1)
    visited = set()
    node4.neighbors = [node3, node2, node1]
    node3.neighbors = [node4]
    node2.neighbors = [node4, node5]
    node1.neighbors = [node4]
    node5.neighbors = [node2]
    # dfs_graph_1(node4, visited)
    dfs_graph(node4)
    # bfs_graph(node4)




