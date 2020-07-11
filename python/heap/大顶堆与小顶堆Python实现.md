# 大顶堆与小顶堆的Python实现

## 目的：求数组中的第k小数和第k大数

```python
import heaqp 
from heaqp import heappush, heapreplace, nlargest, nsmallest

class KSmallest(object):
    """
    构造大顶堆，求数组中第K小的数
    """
    def __init__(self, k, arr):
        self.pool = nsmallest(k, arr)
        self.pool = [-x for x in self.pool]
        heapify(self.pool)
        self.k = k
        
    def add(self, ele):
        ele = - ele
        if len(self.pool) < self.k:
            heappush(self.pool, ele)
        else:
            if self.pool[0] < ele:
                heapreplace(self.pool, ele)
        return -self.pool[0]
    
class KLargest(object):
    """
    构造小顶堆，求数组中第K大的数
    """
    def __init__(self, k, arr):
        self.pool = nlargest(k, arr)
        heapify(self.pool)
        self.k = k
        
    def add(self, ele):
        if len(self.pool) < self.k:
            heappush(self.pool, ele)
        else:
            if self.pool[0] < ele:
                heapreplace(self.pool, ele)
        return self.pool[0]
            
```

