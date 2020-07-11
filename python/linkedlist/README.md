# 链表类题目解题思路

## 206反转链表

解题思路如下图所示
![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/206.jpg)

### 代码如下

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
# 双指针法，一个指针指向前序节点，一个指针指向当前节点，依次循环

"""
class Solution(object):
    def reverseList(self, head):

        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
```



## 92 反转链表2

### 方法二: 迭代链接反转

#### 直觉

迭代法需要一次扫描，首先在翻转链表时需要两个指针，prev和cur来实现链表翻转。此外还需要两个指针保存指向第m个节点及m个节点的前一个节点， 用于保存在上个方法中，

#### 算法

具体如下图所示

##### Step1：cur和prev指针遍历到m结点和m-1结点

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/92_1.png)

##### Step2：使用con和tail指针保留prev和cur指针的位置，用于链表连接

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/92_2.png)

##### Step3：prev和cur继续遍历，并反转从m结点到n结点的链表

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/92_3.png)

##### Step4：使用con和tail指针重新调整链表

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/92_4.png)

#### 复杂度分析

- 时间复杂度: O(N)。考虑包含 N个结点的链表。对每个节点最多会处理（第 n个结点之后的结点不处理）。
- 空间复杂度: O(1)。我们仅仅在原有链表的基础上调整了一些指针，只使用了 O(1)O(1) 的额外存储空间来获得结果。

### 代码如下

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        # judge empty linked list
        if not head:
            return None

        # move the two pointers until they reach the proper starting point in the list
        cur, prev = head, None
        while m > 1:
            cur, prev = cur.next, cur
            m, n = m - 1, n - 1

        # the two pointers that will fix the final connections
        con, tail = prev, cur

        while n:
            cur.next, prev, cur = prev, cur, cur.next
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
```



## 141 判断链表是否有环

### 解题思路1

使用哈希结构表中的set数据结构，依次遍历链表，如果有结点重复出现，则说明链表中存在环，否则，链表无环。

代码如下

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 方法1：使用set
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        result = set()
        cur = head
        while cur:
            if cur in result:
                return True
            result.add(cur)
            cur = cur.next
        return False
```



### 解题思路2

用两个快慢指针，快指针每次走两步，慢指针每次走一步。如果链表中存在环，则快慢指针必然相遇，否则，链表无环的话，快慢指针永远也不会相遇。

代码如下：

```python
# 快慢指针法
    def hasCycle_1(self, head):
        if not head or not head.next:
            return False

        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
```

## 142 判断链表是否有环，并返回链表中入环处的节点

### 解题思路1

使用哈希表中的set数据结构，如果链表有环，则第一个重复出现的节点就一定是链表入环处的节点，该算法的时间复杂度为O(N)，空间复杂度为O(N)。

代码如下：

```python
class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 方法1，使用set数据结果，返回第一个重复的节点
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
                head = head.next
        return None
```



### 解题思路2

使用快慢指针，快指针每次走两步，慢指针每次走一步，如果链表有环，则快慢指针一定会相遇，当快慢指针相遇后，快指针从head节点重新开始遍历，每次走一步，同时，慢指针也继续遍历，直到两者再次相遇，相遇处的节点就是入环的第一个节点。时间复杂度O(N)， 空间复杂度O(1)。

代码如下：

```python
# 方法2，使用快慢指针，当快慢指针第一次相遇时，将快指针置于head， 然后快慢指针再次相遇的节点即为链表环的入口处
    def detectCycle_1(self, head):
        if not head or not head.next:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast
    
     def detectCycle_2(self, head):
        if not head or not head.next:
            return
        fast = slow = head
        while True:
            if not fast or not fast.next:
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next

        return fast
```

## 24 两两反转链表中的节点

### 题目描述

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

### 解题思路1: 迭代法

#### 想法

使用三个变量,分别保存相邻两个交换的节点,以及要迭代的位置, 依次循环下去,直到链表末尾.

#### 算法

- 使用一个哑节点(dummy)用于和原始列表进行链接,方便对链表的处理;
- 使用pre指针来遍历列表,pre指向dummy节点,pre.next指向head节点;
- 保存两个相邻节点的引用, a = pre.next 和b = a.next;
- 交换这两个相邻节点,更新pre节点;
- 循环条件是pre.next和pre.next.next都不为None,对于链表长度为偶数的,都需要交换,对于链表长度为奇数的,最后一个奇结点不需要处理;

#### 算法示意图

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/24_1.jpg)

#### 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        
         # 增加一个dummy节点，处理方便
        dummy = ListNode(-1)
        pre, pre.next = dummy, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy.next
```

#### 复杂度分析

- 时间复杂度：O(n)
- 空间复杂度:O(1)

### 解题思路2: 递归法

#### 算法示意图

https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/dong-hua-yan-shi-24-liang-liang-jiao-huan-lian-bia/

```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # 递归解决
        # 1 递归终止条件
        if not (head and head.next):
            return head
        # 2 假设链表为 1 -> 2 -> 3 -> 4
        # 保存结点2
        tmp = head.next
        # 继续递归,处理 3-> 4
        # 递归结束后, 变成了4->3
        # 于是head结点就指向了4, 变成了1->4->3
        head.next = self.swapPairs(tmp.next)
        # 将结点2指向head
        tmp.next = head
        return tmp
```

## 25 K个1组翻转链表

### 解题思路

[解题思路]: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/di-gui-si-wei-ru-he-tiao-chu-xi-jie-by-labuladong/

简单总结:

- 先去翻转前k个链表元素,可以参考翻转链表那个题,将链表的结尾判定条件由null给为第k个元素,然后将前k个链表与第k+1个元素链表链接起来,接着去递归的翻转第2个k,,第3个k,..., 一直到最后.

#### 递归代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if  not head:
            return head
    # 区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        
        # 反转前 k 个元素
        new_head = self.reverse(a, b)
        # 递归反转后续链表并连接起来
        a.next = self.reverseKGroup(b, k)
        return new_head

    def reverse(self, a, b):

        pre, cur = None, a
        # while 终止的条件改一下就行了
        while  cur != b:
            cur.next, pre, cur = pre, cur, cur.next
        # 返回反转后的头结点
        return pre
```

#### 迭代写法

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head
        pre =  tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail: break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                pre.next = cur.next  # pre和cur.next连接起来, 此时cur(孤单)掉了出来
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变pre和tail的值
            pre = head
            tail = head
        return dummy.next
```

 ## 19. 删除链表的倒数第N个节点

### 解题思路1:两次遍历法

问题简化为删除链表证书第L-N+1位置的节点,只要知道L就可以解决问题.

使用两次遍历,第一次遍历整个链表,获取链表长度记为L, 第二次遍历到L-N节点处(即倒数第N个节点的前一个节点),然后将L-N处的节点与L-N+2处的节点相连,就实现了倒数第N个节点的删除.代码如下:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first:
            length  += 1
            first = first.next

        length_n = length - n
        second = dummy
        while length_n > 0 :
            second = second.next
            length_n -= 1
        second.next = second.next.next
        return dummy.next
```

### 解题思路2: 一次遍历法

使用两个指针, frist和second, 将first指针遍历到N+1个节点处,第二个指针在head处,之后,两个指针同事向链表末尾移动,当frist指针到达末尾时, second指针到达了倒数第N-1个位置,然后将second指针指向倒数第N-1个位置即可.代码如下:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for i in range(n+1):
            first = first.next
            
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
```

## 21合并两个有序链表

方法 1：递归
想法

我们可以如下递归地定义在两个链表里的 merge 操作（忽略边界情况，比如空链表等）：

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/21.jpg)


也就是说，两个链表头部较小的一个与剩下元素的 merge 操作结果合并。

算法
我们直接将以上递归过程建模，首先考虑边界情况。
特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表。否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值。如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

#### 方法2: 迭代
想法

我们可以用迭代的方法来实现上述算法。我们假设 l1 元素严格比 l2元素少，我们可以将 l2 中的元素逐一插入 l1 中正确的位置。

### 算法

首先，我们设定一个哨兵节点 "prehead" ，这可以在最后让我们比较容易地返回合并后的链表。我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。然后，我们重复以下过程，直到 l1 或者 l2 指向了 null ：如果 l1 当前位置的值小于等于 l2 ，我们就把 l1 的值接在 prev 节点的后面同时将 l1 指针往后移一个。否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都把 prev 向后移一个元素。

在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，所以不管哪个链表是非空的，它包含的所有元素都比前面已经合并链表中的所有元素都要大。这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表。

代码如下:

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        
        return dummy.next
```

## 83 删除排序链表中的重复元素

### 解题思路

使用1个指针从链表头开始遍历链表, 如果链表中出现两个节点的值一样,则把当前节点的值链到下一个元素之后的节点,否则,继续循环,直到链表末尾.

### 代码如下

```python
def deleteDuplicates(head):
	if not (head and head.next):
		return head
	cur = head
	while True:
		if cur.val == cur.next.val:
			cur.next = cur.next.next
		else:
			cur = cur.next
		if not cur.next:
        	break
     return head
```

## 82 删除排序链表中的重复节点II

解题思路如下图所示

![](/home/rapheal-wu/learning/AlgorithmReview/AlgoSolutionInLeetcode/AlgoSolutionInLeetcode/LinkedList/82.jpg)

代码如下:

```python
def	deleteDuplicates(head):
	dummy = ListNode(-1)
	dummy.next = head
	pre, cur = None, head
	while cur:
		pre, cur = cur, cur.next
		while cur and cur.next and cur.val == cur.next.val:
			t = cur.val
			while cur and cur.val == t:
				cur = cur.next
		pre.next = cur
	return dummy.next
```

