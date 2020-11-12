# 题目描述
# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#  
#
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#  
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertationSortList(self, head):
        dummy = ListNode(float('inf'))
        cur = dummy.next = head
        while cur and cur.next:
            if cur.next.val > cur.val:
                cur = cur.next
            else:
                # 暂存cur.next, 保留带插入的节点位置(指针)
                nxt = cur.next
                # 将cur结点指向下下一个结点, 将待插入的结点空出来
                cur.next = nxt.next
                # 使用pre指针寻找第一个待插入排序的点的位置
                pre = dummy
                while pre.next and pre.next.val < nxt.val:
                    pre = pre.next
                # 此时已找到待插入的位置
                nxt.next = pre.next
                pre.next = nxt
        return dummy.next

    def insert_sort(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = head, head.next
        while cur is not None:
            tmp = cur.next
            if pre.val > cur.val:
                start = dummy
                while cur.val > start.next.val:
                    start = start.next
                pre.next = cur.next
                cur.next = start.next
                start.next = cur
                cur = tmp
            else:
                pre, cur = pre.next, cur.next
        return dummy.next


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
res = Solution().insert_sort(head)
while res:
    print(res.val)
    res = res.next
