# 题目描述
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#  
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#  
#
# 说明：
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 解题思路1:
# 1 定义一个哨兵节点, 2 定义一个start节点,用来标记每轮(k次)翻转链表前的头结点, 一开始为head; 3 一个flag标志位,用来标记是否剩余节点数量小于k个
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_k_group(self, head, k):
        dummy = ListNode(-1)
        pre, start = dummy, head
        flag = True
        while head:
            for _ in range(k):
                if not head:
                    # 剩余节点数量小于k个,直接退出
                    flag = False
                    break
                head = head.next
            if not flag:
                break
            # 上次翻转后的节点连接这次翻转后的节点
            pre.next = self.reverse_list(start, head)
            # 连接这次翻转以后的正常节点
            start.next = head
            # 更新位置
            pre = start
            start = head
        return dummy.next

    def reverse_list(self, start, end):
        pre, cur = None, start
        while cur != end:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

res = Solution().reverse_k_group(node, 3)
while res:
    print(res.val)
    res = res.next


