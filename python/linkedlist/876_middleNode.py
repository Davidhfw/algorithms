# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        if not head:
            return None
        # calculate the length of head
        first = head
        length = 0
        while first:
            length += 1
            first = first.next
        first = head
        cycle = length // 2
        while cycle != 0:
            cycle -= 1
            first = first.next
        return first
    def middle_node(self, head):
        if head is None:
            return head
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = ListNode(3)
    n1.next.next.next = ListNode(4)
    n1.next.next.next.next = ListNode(5)
    n1.next.next.next.next.next = ListNode(6)
    s = Solution().middle_node(n1)
    while s:
        print(s.val)
        s = s.next