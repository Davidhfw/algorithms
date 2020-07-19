
"""
设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。

解题思路
1、定义循环变量 front 和 rear 。一直保持这个定义，到底是先赋值还是先移动指针就很容易想清楚了。

front：指向队列头部第 1 个有效数据的位置；
rear：指向队列尾部（即最后 1 个有效数据）的下一个位置，即下一个从队尾入队元素的位置。
（说明：这个定义是依据“动态数组”的定义模仿而来。）

2、为了避免“队列为空”和“队列为满”的判别条件冲突，我们有意浪费了一个位置。

浪费一个位置是指：循环数组中任何时刻一定至少有一个位置不存放有效元素。

判别队列为空的条件是：front == rear;；

判别队列为满的条件是：(rear + 1) % capacity == front;。可以这样理解，当 rear 循环到数组的前面，要从后面追上 front，还差一格的时候，判定队列为满。
1、定义循环变量 front 和 rear 。一直保持这个定义，到底是先赋值还是先移动指针就很容易想清楚了。

front：指向队列头部第 1 个有效数据的位置；
rear：指向队列尾部（即最后 1 个有效数据）的下一个位置，即下一个从队尾入队元素的位置。
（说明：这个定义是依据“动态数组”的定义模仿而来。）

2、为了避免“队列为空”和“队列为满”的判别条件冲突，我们有意浪费了一个位置。

浪费一个位置是指：循环数组中任何时刻一定至少有一个位置不存放有效元素。

判别队列为空的条件是：front == rear;；

判别队列为满的条件是：(rear + 1) % capacity == front;。可以这样理解，当 rear 循环到数组的前面，要从后面追上 front，还差一格的时候，判定队列为满。

3、因为有循环的出现，要特别注意处理数组下标可能越界的情况。

（1）指针后移的时候，索引 + 1，要取模；

（2）指针前移的时候，为了循环到数组的末尾，需要先加上数组的长度，然后再对数组长度取模。

"""


class MyCircularDeque(object):
    def __init__(self, k):
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        self.arr = [0 for _ in range(self.capacity)]

    def insertFront(self, value):
        if self.isFull():
            return False
        # 计算位置
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        # 计算位置
        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        # 计算位置
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity


if __name__=="__main__":
    mcd = MyCircularDeque(4)
    print(mcd.insertLast(1))
    print(mcd.insertLast(2))
    mcd.insertFront(3)
    mcd.insertFront(4)
    mcd.getRear()
    mcd.isFull()
    mcd.deleteLast()
    mcd.insertFront(4)
    mcd.getFront()




