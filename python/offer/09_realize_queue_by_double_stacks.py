"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
解题思路：使用两个栈，一个用作入队，一个用作出队，从尾部添加元素时直接将元素加入到入栈中，从头部删除元素时，如果出栈不为空，则直接从出栈顶弹出元素，如果入栈大小为0，表明没有元素，则直接返回-1，
如果出栈大小为0，依次将入栈中的元素弹出并压入出栈中，然后返回出栈栈顶元素
"""
class CQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        if len(self.in_stack)==0:
            return -1
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
