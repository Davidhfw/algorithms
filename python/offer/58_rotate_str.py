def rotate_words(str, k):
    if not str or len(str) == 0:
        return str
    return str[k:] + str[:k]


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(rotate_words(s, k))
