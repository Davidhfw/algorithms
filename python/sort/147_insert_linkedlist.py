import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def insertionSortList(self, head):

        """
        例题演示
        0： d -> 2 -> 1 -> 4 -> 3
        1:  d -> 2 -> 1 -> 4 -> 3
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy  # 记录哑结点并用其作为内层循环遍历的起点
        cur = head
        while cur:
            lat = cur.next  # 记录当前节点的下一个节点
            # 如果下个节点lat比当前节点cur小
            if lat and lat.val < cur.val:
                cur.next = lat.next  # 跳过要插入排序的下个节点lat
                while pre.next and pre.next.val < lat.val:
                    # 用pre来遍历前面已经排好的链表，找入插入点
                    pre = pre.next
                lat.next = pre.next  # 插入节点lat在pre和pre.next之间
                pre.next = lat
                pre = dummy  # 让pre恢复到哑节点
            else:
                cur = lat
        return dummy.next


if __name__ == '__main__':
    node = ListNode(4)
    node.next = ListNode(2)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(3)
    start = time.time()
    new_head = Solution().insertionSortList(node)
    end = time.time()
    print("Running cost time is ", (end - start) * 10000000)
    while new_head:
        print(new_head.val)
        print('->')
        new_head = new_head.next

