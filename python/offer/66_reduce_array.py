def constructorArr(a):
    b, tmp = [1] * len(a), 1
    for i in range(1, len(a)):
        # 下三角
        b[i] = b[i-1] * a[i-1]
    for i in range(len(a) - 2, -1, -1):
        # 上三角
        tmp *= a[i+1]
        # 下三角 * 上三角
        b[i] *= tmp
    return b


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(constructorArr(a))
