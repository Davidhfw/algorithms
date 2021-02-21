import queue
import collections


class MaxQueue(object):
    def __init__(self):
        self.deque = collections.deque()
        self.queue = queue.Queue()

    def max_value(self):
        return self.deque[0] if self.deque else -1

    def push_back(self, value):
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self):
        if not self.deque:
            return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
