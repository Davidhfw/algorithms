"""
验证二叉搜索树的后序遍历序列
"""
def verify_post_order(post_order):
    def recur(i, j):
        # 节点遍历结束
        if i >= j:
            return True
        p = i
        # 左子树所有节点值大于根节点值
        while post_order[p] < post_order[j]:
            p += 1
        m = p
        # 右子树所有节点值大于根节点值
        while post_order[p] > post_order[j]:
            p += 1
        # 递归遍历左右子序列
        return p == j and recur(i, m -1) and recur(m, j - 1)
    return recur(0, len(post_order) - 1)


post_order = [1, 3, 2, 6, 5]
print(verify_post_order(post_order))
"""

"""




