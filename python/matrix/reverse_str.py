def reverseWords(s):
    s_tmp = s.split(" ")
    print(s_tmp)
    for i in range(len(s_tmp)):
        left, right = 0, len(s_tmp[i]) - 1
        print(left)
        print(right)
        print(type(s_tmp))
        while left < right:
            s_tmp[i][left], s_tmp[i][right] = s_tmp[i][left], s_tmp[i][right]
            left += 1
            right -= 1
    res = ''
    for i in range(len(s_tmp)):
        res += ' '
    return res


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverseWords(s))