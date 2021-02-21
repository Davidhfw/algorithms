'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
解题思路：使用栈存储节点值，然后返回反转栈
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
