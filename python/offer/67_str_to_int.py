def str_to_int(s):
    if not s:
        return 0
    # 去除字符串头尾空格
    s = s.strip()
    # sign表示符号位
    res, i, sign = 0, 1, 1
    # 最大值与最小值标记
    max_value, min_value, bandry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
    # 处理字符串第一个元素， 符号位
    if s[0] == '-':
        sign = -1
    elif s[0] != '+':
        i = 0
    for c in s[i:]:
        if not '0' <= c <= '9':
            break
        if res > bandry or res == bandry and c > '7':
            return max_value if sign == 1 else min_value
        res = 10 * res + ord(c) - ord('0')  # 数字拼写

    return sign * res


if __name__ == '__main__':
    sl = ["42", "    -42", "4193 with words", "words and 987", "-91283472332", "91283472332"]
    for s in sl:
        print(str_to_int(s))


