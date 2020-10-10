class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点head和tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_header(self, key):
        #　先将哈希表key指向的节点领出来，
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 之后将node插入到头部节点前
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node



