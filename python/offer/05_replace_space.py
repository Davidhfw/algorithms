"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
解题思路：正则替换或者字符串分割，然后使用%20拼接起来
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s or s == "":
            return s
        new_s = ''
        for i in s:
            if i == ' ':
                i = '%20'
            new_s += i
        return new_s
