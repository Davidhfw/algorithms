def bubble_sort(arr):
    # 处理异常情况
    if not arr or len(arr) <= 1:
        return arr
    n = len(arr)
    # 外层循环控制从头走到尾的过程
    for i in range(n):
        count = 0
        # 内层循环控制走一遍的过程
        # 进行两两比较，如果发现当前的数比下一个数还大，那就发生交换，同时记录下有交换发生的次数
        for j in range(0, n - 1 - i): # 这里取n - 1 -i ,是为了避免arr[j+1]时,数组访问下标越界
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
        if count == 0:
            break
    return arr


nums = [ 3, 8, 0, 4, 2, 5, 9]
print(bubble_sort(nums))
