# 二分查找最简单的情况， 数组中元素都是顺序排列而且没有重复的元素

def binary_search_0(arr, target):
    if not arr or len(arr) == 0:
        return
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 变体， 数组中存在重复的元素， 查找第一个值等于给定值的元素
def binary_search_1(arr, target):
    if not arr or len(arr) == 0:
        return
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    while left <= right:
        mid = left + ((right - left ) >> 1)
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                right = mid - 1
    return False

# 变体2，查找最后一个值等于给定值的元素
def binary_search_2(arr, target):
    if not arr or len(arr) == 0:
        return
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            if mid == arr_len-1 or arr[mid + 1] != target:
                return mid
            else:
                left = mid + 1
    return False

# 变体3， 查找第一个大于等于给定值的元素
def binary_search_3(arr, target):
    if not arr or len(arr) == 0:
        return
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] >= target:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            else:
                right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return False

# 变体4，查找最后一个小于等于给定值的元素
def binary_search_4(arr, target):
    if not arr or len(arr) == 0:
        return
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if arr[mid] <= target:
            if mid == arr_len - 1 or arr[mid + 1] > target:
                return mid
            else:
                left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return False