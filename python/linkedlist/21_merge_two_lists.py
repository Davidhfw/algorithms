# 题目描述
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 解题思路: 新建一个亚节点, 通过两个链表中的节点值大小,每次将较小的节点加入哑节点的链表中, 直到最终完成节点计算

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge_two_lists(self, list1, list2):
        dummy = ListNode(-1)
        pre = dummy

        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next
        pre.next = list1 if list1 else list2
        return dummy.next
