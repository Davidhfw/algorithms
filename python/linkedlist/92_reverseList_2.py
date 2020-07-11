class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        # judge empty linked list
        if not head:
            return None

        # move the two pointers until they reach the proper starting point in the list
        cur, prev = head, None
        while m > 1:
            cur, prev = cur.next, cur
            m, n = m - 1, n - 1

        # the two pointers that will fix the final connections
        con, tail = prev, cur

        while n:
            cur.next, prev, cur = prev, cur, cur.next
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head



