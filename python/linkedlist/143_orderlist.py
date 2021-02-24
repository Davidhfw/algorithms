
# 重排链表
# 解题思路：1 找到链表中间节点，并将列表分为两个部分 2 反转第二部分列表 3 合并两个列表
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def findMiddlePoint(head):
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseList(head):
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


def mergeLists(l1: Node, l2: Node):
    while l1 and l2:
        l1_tmp, l2_tmp = l1.next, l2.next
        l1.next = l2
        l1 = l1_tmp
        l2.next = l1
        l2 = l2_tmp


def reorderList(head):
    if not head:
        return
    mid = findMiddlePoint(head)
    l1, l2 = head, mid.next
    mid.next = None
    l2 = reverseList(l2)
    mergeLists(l1, l2)


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    reorderList(head)
    while head:
        print(head.val)
        head = head.next
