from time import time

def merge_sort(arr):
    # 归并排序
    # 处理输入值异常
    if not arr or len(arr) <= 1:
        return arr
    # 将列表分成两个更小的列表
    mid = len(arr) // 2

    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left_list, right_list)


def merge(left_list, right_list):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    # 新的已排序号的列表
    result = []
    i = j = 0
    # 对两个列表中的元素，两两对比
    # 将最小的元素添加到result， 并对当前列表下标加1
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    result += left_list[i:]
    result += right_list[j:]
    return result


if __name__ == '__main__':
    start_time = time()
    arr = [5, 0, 8, 7, 2, 90, 100, 345, 1, 2]
    new_arr = merge_sort(arr)
    end_time = time()
    print('sorted arr and cost time is {} and {}'.format(new_arr, (end_time - start_time) * 1000))