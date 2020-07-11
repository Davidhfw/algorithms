import time


def insert_sort(arr):
    # 处理异常
    if not arr or len(arr) <= 1:
        return arr
    n = len(arr)
    # 这里遍历的顺序是, i从1到n-1, j在i到0之间, 假定的是数组前面的值升序排列
    for i in range(1, n):
        # 从后往前比较
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr


def insert_sort_ada(arr):
    # 处理数组异常情况
    if not arr or len(arr) <= 1:
        return arr

    n = len(arr)
    for i in range(1, n):
        # 保存当前值
        key = arr[i]
        # 从当前值的前一个值开始比较,一直到找到合适的插入区间停止
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        # 在插入位置处放入key值
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

