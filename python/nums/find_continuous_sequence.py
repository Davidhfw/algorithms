# 和为s的连续正数序列
# 解题思路：使用双指针，从数组左边开始扩展，当发现数组和小于给定值时，右边界扩大，同时增加序列和；当发现数组和大于给定值时，左边扩大，同时减小序列和，当数组序列和等于
# 给定值时，将左边界和右边界之内的数组加入到列表中，完成数组的统计，同时左边界向右移动，数组和减去左边界值。
def find_continuous_sequence(target):
    i = 1 # 滑动窗口的左边界
    j = 1 # 滑动窗口的右边界
    sums = 0 # 滑动窗口中的数字和
    res = []
    while i <= target // 2:
        if sums < target:
            # 右边界向右移动，扩大滑动窗口大小
            sums += j
            j += 1
        elif sums > target:
            # 左边界向右移动
            sums -= i
            i += 1
        else:
            arr = list(range(i, j))
            res.append(arr)
            sums -= i
            i += 1
    return res


target = 18
print(find_continuous_sequence(target))