'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
解题思路：使用前序遍历获取根节点，然后使用一个存储了中序遍历中值与下标对应的哈希表，找到根节点对应的下标，将序列划分为左右两个子树，递归重建左右子树
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(root, left, right):
            if left > right:
                return # 递归终止
            # root代表根节点的下标值
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i+1, right)
            return node
        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)
