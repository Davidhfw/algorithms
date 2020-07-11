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
            # 合并区间如[1,4]和[3, 6],或者[1, 6]和[2, 3]
            else:
                res[-1][1] = max(s[1], res[-1][1])
        return res


if __name__ == '__main__':
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    seq = Solution().merge(intervals)
    print('seq is ', seq)
    seq_1 = Solution().merge_1(intervals)