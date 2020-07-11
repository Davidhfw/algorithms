# 排序经典算法总结
## 冒泡排序
### 算法思想
两两比较数组中的相邻元素，记两个相邻的元素为a[i]和a[i+1]， 如果a[i]大于a[i+1], 则交换着这两个元素的顺序，并将本次交换值加一，依次遍历到数组末尾，这样就能保证这一轮过后，数组的最后一个元素为全
组最大的元素，之后再依次遍历除最后一个元素之外的数组其他元素，这里需要执行两个for循环，因此他的时间复杂度为O(n^2),空间复杂度为O(1)
### 代码如下
```python
def bubble_sort(arr):
    arr_len = len(arr)
    # 外层循环控制从头走到尾的过程
    for i in range(arr_len):
        count = 0
        # 内层循环控制走一遍的过程
        # 进行两两比较，如果发现当前的数比下一个数还大，那就发生交换，同时记录下有交换发生的次数
        for j in range(0, arr_len -1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
        if count == 0:
            break
```
## 插入排序
### 基本思想
不断将尚未拍好序的数插入到已经排好序的部分
### 特点
在冒泡排序中，经过每一轮的排序处理后，数组后端的数是排好序的；而对于插入排序来说，经过每一轮的排序处理后，数据前端的数都是排好序的。
### 例题分析
对数组[2, 1, 7, 9, 5, 8]进行插入排序。
### 解题思路
首先将数组分成左右两个部分，左边是已经排好序的部分，右边是还没有排好序的部分，刚开始，左边已排好序的部分只有一个元素2。接下来，我们对右边的元素一个一个进行处理，将他们放到左边。
1. 先来看1， 由于1比2小，需要将1插入到2的前面，做法很简单，两两交换位置即可，[1, 2, 7, 9, 5, 8]。
2. 然后，我们要把7插入到左边的部分，由于7已经比2大了，表明他是目前最大的元素，保持位置不变，[1, 2, 7, 9, 5, 8]。
3. 同理，9也不需要做位置变动，[1, 2, 7, 9, 5, 8]。
4. 接下来，如何把5插入到合适的位置。首先比较5和9，由于5比9小，两两交换，[1, 2, 7, 5, 9, 8]。继续，由于5比7小，两两交换，
[1, 2, 5, 7, 9, 8]。最后，由于5比2大，本轮结束。
5. 最后一个数是8， 由于8比9小，两两交换，[1, 2, 5, 7, 8, 9]，再比较7和8，发现8比7大，此轮结束。到此，插入排序完毕。
### 代码如下
```python
import time


def insert_sort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    for i in range(1, arr_len):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


def insert_sort_ada(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    for i in range(1, arr_len):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [2, 1, 7, 5, 8, 9, 3]
t1_start = time.time()
new_arr1 = insert_sort(arr)
t1_end = time.time()
print('insert sort before ada cost time is', t1_end - t1_start)

t2_start = time.time()
new_arr2 = insert_sort(arr)
t2_end = time.time()
print('insert sort after ada cost time is', t2_end - t2_start)

```
### 复杂度分析
- 时间复杂度：O(n^2)
- 空间复杂度：O(1)
## 快速排序
### 解题思路
https://www.cnblogs.com/kaiping23/p/9614395.html
https://www.cnblogs.com/geogre123/p/11127154.html
### 代码
```python
# 非递归方式
def quick_sort(arr, start, end):
    # 分治，一分为二
    # start == end， 表明要处理的数组元素只有一个
    # start > end, 表明右边没有数据
    if start >= end:
        return
    # 定义两个游标， 分别指向数组的起始和末尾
    left, right = start, end
    # 取快排的基准元素作为标记, 一般取数组第一个元素
    mid = arr[left]
    while left < right:
        # 让右边右边往左移动， 目的是找到比mid小的元素,放大left游标的位置
        while left < right and arr[right] >= mid:
            right -= 1
        arr[left] = arr[right]
        # 让左边游标向右移动，目的是找到比mid大的元素，将该元素放到right游标处的位置
        while left < right and arr[left] < mid:
            left += 1
        arr[right] = arr[left]
    # while结束后， 将mid放到中间位置， left=right
    arr[left] = mid
    # 递归处理左边的数据
    quick_sort(arr, start, left - 1)
    # 递归处理右边的数据
    quick_sort(arr, left + 1, end)
    return arr


if __name__ == '__main__':
    arr = [7, 9, 2, 0, 40, 88, 5, 3, 100]
    new_arr = quick_sort(arr, 0, len(arr) - 1)
    print('new_arr is ', new_arr)

```
## 归并排序
### 归并排序
归并排序是创建在归并操作上的一种有效的排序算法。时间复杂度为O(nlogn)。该算法是采用分治法是一个典型的应用，且各层分治递归同时进行。
### 分治法
字面意思是分而治之，就是把一个复杂问题分成两个或多个相同或相似的子问题。再把子问题分成更小的子问题。直到最后子问题可以简单求解。原问题的解即子问题的合并。
### 设计思想
将一个难以直接解决的大问题，分割成规模较小的相同问题，分而治之，各个击破。
### 基本步骤
- step1 分解：将原问题分解成若干规模较小。相互独立，与原问题形式相同的子问题。
- step2 解决：若子问题规模较小，则直接解决，否则递归解决子问题。
- step3 合并：将各个子问题的解合并为原问题的解。
### 思维过程
实际上就是类似于数学归纳法，找到解决本问题的求解方程公式，然后根据方程公式设计递归程序。
1. 一定是先找到最小问题规模时的求解方法
2. 然后考虑随着问题规模增大时的求解方法
3. 找到求解的递归函数式后（各种规模或因子），设计递归程序即可
### 举例
arr = [5, 3, 2, 0, 1, 4]
1. 首先寻找最小规模的求解方法
如 left=[5]，right=[3]
将两个列表合并成一个有序的列表
```python
result = []
if left[0] <= right[0]:
    result.append(left[0])
else:
    result.append(right[0])
result += left
```
此时 合并后的列表 result = [3,5]就是排序好的列表。
2. 现在我们将问题的规模扩大。
left = [0,3,5] right = [1,4]
将两个有序列表，合并成一个有序列表：
比较二个列表的第一个数，谁小就先取谁，取了后就在对应的列表中跳过这个数。然后再进行比较，如果有如果为空，那直接将另一个列表的数据依次取出即可：
```python
result = []
i = 0 #left列表的下标
j = 0 #right列表的下标
while i < len(left) and j < len(right):
if left[i] <= right[j]:
result.append(left[i])
i += 1
else：
result.append(right[j])
j += 1
result = left[i:] #将剩余的元素合并到新的列表中
result = right[j:] #将剩余的元素合并到新的列表中。
此时 合并后的列表 result = [0,1,3,4,5]就是排序好的列表。
```
3. 设计递归，将复杂的问题分解为最小规模子问题。
 - 将列表分解为 两个更小的列表。
-  递归分解，将更小的列表继续分解，直到达到最小规模，也就是只有一个元素的时候。
- 对已经排序好的列表 进行合并。单个元素的列表，认为是已经排序好的。
- 最小规模，列表只有一个元素的时候。
```python
if len(seq) <= 1:
    return seq
```
```python
mid = len(seq)/2 
```
#将列表分成更小的两个列表
分别对左右两个列表进行递归分解
```python
left = mergesort(seq[:mid])
right = mergesort(seq[mid:])
```
对排序好的两个列表合并，产生一个新的排序好的列表
```python
return merge(left,right)
```
### 代码如下
```python
def merge_sort(arr):
    # 归并排序
    if len(arr) <= 1:
        return arr
    # 将列表分成两个更小的列表
    mid = len(arr) // 2

    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 新的已排序号的列表
    result = []
    i = 0
    j = 0
    # 对两个列表中的元素，两两对比
    # 将最小的元素添加到result， 并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    arr = [5, 0, 8, 7, 2, 90, 100, 345, 1, 2]
    new_arr = merge_sort(arr)
    print('new_arr is ', new_arr)
```
## 56 合并区间
### 解题思路
从第二个区间开始（i=1），对于第i个区间，一共只有三种情况，并且保证每次对第i个区间只进行删除或不变两种操作，对第i-1个区间只进行合并或不变两种操作：
if 第i个区间的左边界(seq[i][0])落入第i-1个区间：

1. 若第i个区间的右边界(seq[i][1]) ≥ 第i-1个区间的右边界(seq[i-1][1]):
    比如第i个区间是[3,6],第i-1个区间是[1,4]，那么区间[3,6]删除，区间[1,4]--->[1,6] 合并

2. 若第i个区间的右边界(seq[i][1]) ≤ 第i-1个区间的右边界(seq[i-1][1]):
    比如第i个区间是[3,4],第i-1个区间是[1,4]，那么区间[3,4]删除，区间[1,4]--->[1,4] 不变
else:
比如[1,4],[6,9]

3. 此时第i与第i-1个区间不能合并，搜索下一个区间，判断是否能与[6,9]区间发生合并
### 代码如下：
```python
class Solution:

    def merge(self, intervals):
        seq = sorted(intervals)  # 区间从小到大排序，若左边界相等，则对右边界排序；
        i = 1  # 初始位置从第二个区间开始
        while i < len(seq):
            if seq[i][0] >= seq[i - 1][0] and seq[i][0] <= seq[i - 1][1]:
                if seq[i][1] <= seq[i - 1][1]:
                    seq.remove(seq[i])
                else:
                    seq[i - 1] = [seq[i - 1][0], seq[i][1]]
                    seq.remove(seq[i])
            else:
                i += 1
        return seq

    def merge_1(self, intervals):
        # 按列表中每个列表元素的第一个值升序排序
        seq = sorted(intervals, key=lambda x: x[0])
        res = []
        for s in seq:
            # 不合并区间
            if not res or res[-1][1] < s[0]:
                res.append(s)
            # 合并区间如[1,4], [3, 6]
            else:
                res[-1][1] = max(s[1], res[-1][1])
        return res
if __name__ == '__main__':
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    seq = Solution().merge(intervals)
    print('seq is ', seq)
```
