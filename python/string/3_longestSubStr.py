# 题目描述: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 解题思路:
# 1 滑动窗口
# 从左侧开始遍历S，以i标记窗口左侧，j标记窗口右侧，初始时，i=0，j=0，即开头a所在的位置，此时，窗口大小为1
#
# 然后，将j右移，逐步扩大窗口，依次经过b、c、d，此时，窗口内均无重复字符，继续右移j
# 当j移动到d后面的a所在位置时，对应字符a在窗口中已存在，此时，窗口大小为5，去除当前重复的一位，窗口大小为4。此时窗口内的字符串abcd为
# 找到窗口中已存在的该字符所在位置，并将i移动到该位置下一位
# 此时为第二个窗口
# 继续重复之前的操作，直到j移动到字符串最后一位停止。
# 代码规范
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s or len(s) < 1:
            return 0
        n = len(s)
        res = []
        max_len, cur_len = 0, 0
        for i in range(n):
            val = s[i]
            if val not in res:
                res.append(val)
                cur_len += 1
            else:
                index = res.index(val)
                res = res[index+1:]
                res.append(val)
                cur_len = len(res)
            max_len = max(max_len, cur_len)
        return max_len

    def lengthOfLongestSubString1(self, s):
        # 异常情况处理
        if not s or len(s) < 1:
            return 0
        # st记录s中每个字符的下标
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            # 如果遇到重复字符,更新i的值, 将i的值更新到第一个重复元素出现的位置
            if s[j] in st:
                i = max(st[s[j]], i)
            # 更新最长子串的长度
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


s = 'abcdafg'
print(Solution().lengthOfLongestSubString1(s))
