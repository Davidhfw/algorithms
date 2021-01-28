"""
题目介绍：剑指 Offer 48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度
"""
def length_of_longest_substring(s):
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        # 获取索引i
        i = dic.get(s[j], -1)
        # 更新哈希表
        dic[s[j]] = j
        tmp = tmp + 1 if tmp < j - i else j - i
        res = max(res, tmp)
    return res


s='abcdefgabcdabcikghjk'
print(length_of_longest_substring(s))

def singleNumber(nums):
    counts = [0] * 32
    for num in nums:
        for j in range(32):
            counts[j] += num & 1
            num >>= 1
    res, m = 0, 3
    for i in range(32):
        res <<= 1
        res |= counts[31 - i] % m
    return res if counts[31] % m == 0 else ~( res ^ 0xffffffff)