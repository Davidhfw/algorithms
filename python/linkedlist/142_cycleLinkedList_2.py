class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 方法1，使用set数据结果，返回第一个重复的节点
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return None

    # 方法2，使用快慢指针，当快慢指针第一次相遇时，将快指针置于head， 然后快慢指针再次相遇的节点即为链表环的入口处
    def detectCycle_1(self, head):
        if not head or not head.next:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast

    def detectCycle_2(self, head):
        if not head or not head.next:
            return
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast



