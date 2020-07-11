class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
# 双指针法，一个指针指向前序节点，一个指针指向当前节点，依次循环
# 递归发:
"""


class Solution(object):
    def reverseList(self, head):

        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList_recursion(self, head):
        # 递归终止条件, 当前节点为空或者当前节点的下一个节点为空
        if not head or not head.next:
            return head
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        cur = self.reverseList_recursion(head.next)
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur, 也就是最后一个节点
        return cur
