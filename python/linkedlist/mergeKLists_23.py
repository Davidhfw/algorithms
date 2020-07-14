"""
题目描述：　合并ｋ个有序链表
解题思路１: 使用优先队列，每次各取ｋ个链表的第一个节点入队列，构建小顶堆，
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    """
    每次只有ｋ个元素入堆，避免一次性入堆所有元素导致堆过大，内存占用过多的问题
    """
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(0)
        # head表示堆
        head = []
        p = dummy
        n = len(lists)
        for i in range(n):
            # 如果输入链表不为空，则加入堆
            if lists[i]:
                # 将ｋ个链表中的第一个元素入堆，并且ｋ个链表指向后面的元素
                """
                |1|->3->4
                |1|->4->5->7
                |2|->6->9
                """
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        # 循环弹出堆中元素
        while head:
            # 弹出堆中最小元素
            val, idx = heapq.heappop(head)
            # 构建新的排序链表
            p.next = ListNode(val)
            p = p.next
            # 如果K个链表中还有节点，将其加入堆中
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    list3 = ListNode(2)
    list3.next = ListNode(6)
    lists = [list1, list2, list3]
    print("lists is ", lists)
    listall = Solution().mergeKLists(lists)
    while listall:
        print(listall.val)
        listall =listall.next
