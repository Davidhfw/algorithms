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
    pivot = arr[left]
    while left < right:
        # 让右边右边往左移动， 目的是找到比pivot小的元素,放大left游标的位置
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        # 让左边游标向右移动，目的是找到比pivot大的元素，将该元素放到right游标处的位置
        while left < right and arr[left] < pivot:
            left += 1
        arr[right] = arr[left]
    # while结束后， 将pivot放到中间位置， left=right
    arr[left] = pivot
    # 递归处理左边的数据
    quick_sort(arr, start, left - 1)
    # 递归处理右边的数据
    quick_sort(arr, left + 1, end)
    return arr


if __name__ == '__main__':
    arr = [7, 9, 2, 0, 0, 40, 88, 5, 3, 5, 6, 100]
    new_arr = quick_sort(arr, 0, len(arr) - 1)
    print('new_arr is ', new_arr)
