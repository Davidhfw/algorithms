class Solution(object):
    def isValid(self, s):

        dct = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            # 如果c不在dct的key中，就将c压入栈中
            if c not in dct:
                stack.append(c)
            # 如果c在dct的key中，则将栈顶元素与c做比较。
            # not stack 确保栈不为空，避免弹出元素时出现溢出的情况。
            elif not stack or dct[c] != stack.pop():
                return False
        # 整个遍历s之后，查看stack是否为空，为空则说明s为有效的括号，否则为非法的括号
        return not stack


if __name__ == '__main__':
    s = '{{{{}}}}[][][()()'
    result = Solution().isValid(s)
    print('result is ', result)