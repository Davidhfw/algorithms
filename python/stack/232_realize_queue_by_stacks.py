# 题目描述: 使用两个栈实现队列
# 解题思路: 使用两个栈, 一个栈用于入栈,另外一个用于出栈
# 1 push操作: 使用入栈将元素添加到队列中
# 2 pop操作: 如果出栈长度为空, 依次将入栈中的元素弹出并添加到出栈中, 然后将出栈中的栈顶元素弹出并返回
# 3 peek操作: 如果出栈长度为空, 依次将入栈中的元素弹出并添加到出栈中, 然后将出栈中的栈顶中最后一个元素返回
# 4 empty操作: 返回入栈和出栈长度为空判断的与操作


class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        if len(self.out_stack) == 0:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


if __name__ == '__main__':
    obj = MyQueue()
    for i in range(5):
        obj.push(i)
    param_2 = obj.pop()
    print('param_2 is ', param_2)
    param_3 = obj.peek()
    print('param_3 is ', param_3)
    param_4 = obj.empty()
    print('param_4 is ', param_4)