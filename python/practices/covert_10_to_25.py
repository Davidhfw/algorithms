def convert_10_to_25(n, base):
    """
    将10进制数转换为25进制
    :param n: 10进制数
    :param base: 带转换的进制
    :return: 转换后的进制数
    """
    base_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ""
    while True:
        s = n // base
        mod = n % base
        result += base_list[mod]
        if s == 0:
            break
        n = s
    return result[::-1]


result = convert_10_to_25(100, 29)
print(result)