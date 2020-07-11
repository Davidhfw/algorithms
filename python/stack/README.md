# 栈题目解题思路及代码总结
## 232：用栈实现队列
### 解题思路
栈的特点是先进后出，队列的特点是先进先出。我们使用两个栈，一个用于入队，另外一个用于出队。
- 入队时将元素压入栈1；
- 出队时，先判断栈2是否为空， 如果为空的话，则将栈1中的元素依次弹出，并依次压入
栈2中，完成之后，然后弹出栈2顶的元素。
- 返回队列头的元素，也是先判断栈2是否为空， 如果为空的话，则将栈1中的元素依次弹出，并依次压入
栈2中，完成之后，然后弹出栈2最后一个元素。
- 队列为空：返回两个栈长度是否为空的与操作。
```python
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
```
## 225 用队列实现栈
### 解题思路
栈的特点是先进后出，队列的特点是先进先出，要使用队列模拟栈， 使用两个队列来模拟栈的输出。一个用于入栈，另一个用于出栈。具体思路如下：
- push：将元素压入队列1。
- pop：将入队列1中的元素依次弹出，只保留一个元素，然后返回，同时交换入队列1和出队列2，本质就是说那个队列不为空，就作为入队列。反之，作为出队列。
- top：返回入队列1中的唯一一个元素。
- empty： 返回两个队列是否为空的与操作
```python
from queue import Queue

class MyStack(object):

    def __init__(self):
        self.in_queue = Queue()
        self.out_queue = Queue()

    def push(self, x):
        self.in_queue.put(x)
        self.top_ele = x

    def pop(self):
        while self.in_queue.qsize() > 1:
            self.top_ele = self.in_queue.get()
            self.out_queue.put(self.top_ele)
        res = self.in_queue.get()
        self.in_queue, self.out_queue = self.out_queue, self.in_queue
        return res

    def top(self):
        return self.top_ele

    def empty(self):
        return self.in_queue.empty() and self.out_queue.empty()


if __name__ == '__main__':
    obj = MyStack()
    for i in range(5):
        obj.push(i)
    param_2 = obj.pop()
    print('param_2 is ', param_2)
    param_3 = obj.top()
    print('param_3 is ', param_3)
    param_4 = obj.empty()
    print('param_4 is ',param_4)
```
## 20 有效括号
### 解题思路
借用栈的数据结构，依次处理每个括号，如果遇到左括号（包括左小括号，左中括号和左大括号），将其压入栈中。
如果碰到右括号（包括右小括号，右中括号和右大括号），则将该括号与栈顶的元素进行匹配，能匹配的上，则将栈顶元素弹出，否则该括号表达式无效。
如果整个元素都遍历完了，栈中的元素个数不为空，则说明该字符串不符合表达式。返回false
### 解题代码
```python
class Solution(object):
    def isValid(self, s):

        dct = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            # 如果c不在dct的key中，就将c压入栈中
            if c not in dct:
                stack.append(c)
            # 如果c在dct的key中，则将栈顶元素与c做比较。
            # not stack 确保栈不为空，避免弹出元素时出现溢出的情况。
            elif not stack or dct[c] != stack.pop():
                return False
        # 整个遍历s之后，查看stack是否为空，为空则说明s为有效的括号，否则为非法的括号
        return not stack


if __name__ == '__main__':
    s = '{{{{}}}}[][][()()'
    result = Solution().isValid(s)
    print('result is ', result)
```