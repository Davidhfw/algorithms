class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # iteration method
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre, pre.next = dummy, head

        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return dummy.next

    def swapPairs_recur(self, head):

        # 递归终止条件:当前节点为空或者下一个节点为空
        if not head or not head.next:
            return head
        # 保存当前节点及下一个节点
        # Nodes to be swapped
        first_node, second_node = head, head.next
        # 将当前节点指向下一次递归
        # Swapping
        first_node.next = self.swapPairs_recur(second_node.next)
        second_node.next = first_node

        return second_node

    def swapPairs_recur1(self, head):
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        l1 = head.next
        head.next = self.swapPairs(head.next.next)
        l1.next = head

        return l1


if __name__ == '__main__':
    # generate linked list
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    # head = Solution().swapPairs(node)
    head = Solution().swapPairs_recur(node)
    while head:
        print(head.val)
        print('->')
        head = head.next