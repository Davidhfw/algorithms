# 题目描述
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
# 解题思路1: 使用快慢指针,快指针用来跳过重复节点, 慢指针用来链接链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicatesII(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev, cur = None, dummy
        while cur:
            prev, cur = cur, cur.next
            while cur and cur.next and cur.next.val == cur.val:
                tmp = cur.val
                while cur and cur.val == tmp:
                    cur = cur.next
            prev.next = cur
        return dummy.next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(5)

res = Solution().deleteDuplicatesII(node)
while res:
    print(res.val)
    res = res.next

