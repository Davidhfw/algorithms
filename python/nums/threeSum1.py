# 题目描述：　给定一个ｎ个数字的数组和目标值，求出数组中符合要求的三个数，使得这三个数等于目标值，注意，不能包含重复值

def three_sum(arr, target):
    # 处理异常情况
    if arr is None:
        return []
    elif len(arr) < 3:
        return []
    # 对数组进行升序排序
    arr.sort()
    ret = []
    n = len(arr)
    # i从０遍历到ｎ-3
    for i in range(n-2):
        # 遇到重复的跳过
        if i > 0 and arr[i] == arr[i-1]:
            continue
        # 两边逼近
        left = i + 1
        right = n - 1
        while left < right:
            sum1 = arr[i] + arr[left] + arr[right]
            if sum1 == target:
                ret.append((arr[i], arr[left], arr[right]))
                # 跳过重复的值
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right -1]:
                    left -= 1
                # 向中间逼近
                left += 1
                right -= 1
            elif sum1 < target:
                left += 1
            else:
                right -= 1
    return ret


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    arr = None
    arr = [1, 2]
    target = -5
    res = three_sum(arr, target)
    print(res)