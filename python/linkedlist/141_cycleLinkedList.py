class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 方法1：使用set
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        result = set()
        cur = head
        while cur:
            if cur in result:
                return True
            result.add(cur)
            cur = cur.next
        return False

    # 快慢指针法
    def hasCycle_1(self, head):
        if not head or not head.next:
            return False

        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

