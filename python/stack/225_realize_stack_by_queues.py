# 使用两个队列实现栈
# 解题思路: 栈的特点是先进后出, 队列特点是先进先出, 一个队列作为入队, 另外一个队列作为出队
# 1 push操作: 将元素放入入队中, 并记录入队元素, 方便后续返回栈顶元素
# 2 pop操作: 判断入队列大小,如果入队列大小大于1, 就将入队列中的元素依次取出并且放入到出队列中, 如果入队列中的元素个数只有一个,此时直接将该元素取出并返回, 并且交互入队列和出队列的位置
# 也就是说, 入队列与出队列的判断标准就是,入队列长度不为空
# 3 top操作: 直接返回2中的元素
# 4 empty操作: 返回入队列和出队列各自empty操作的与结果

from queue import Queue

class MyStack(object):

    def __init__(self):
        self.in_queue = Queue()
        self.out_queue = Queue()
        self.top_ele = None

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