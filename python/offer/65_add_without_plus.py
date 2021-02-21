def add(a, b):

    x = 0xffffffff
    # 如果存在负数则需要转换成补码形式，正数补码是其本身
    a, b = a & x, b & x
    while b != 0:
        # 如果是负数，需要转换成补码形式
        carry = ((a & b) << 1) & x
        a ^= b
        b = carry
        # 如果是正数，则直接返回，反之返回负数的原码
    return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    a1 = -4
    b1 = -9
    print(add(a1, b1))
