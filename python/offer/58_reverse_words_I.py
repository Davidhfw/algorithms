def reverse_words(str):
    if not str or len(str) == 0:
        return str
    str = str.strip()
    str_l = str.split()
    print(str_l)
    return " ".join(str_l[::-1])


def reverse_words_2(s):
    s = s.strip()
    strs = s.split()
    return ' '.join(strs[::-1])


if __name__ == '__main__':
    s = "the sky is blue"
    s1 = "   hello world!   "
    s2 = "a     good    example"
    print(reverse_words(s))
    print(reverse_words(s1))
    print(reverse_words(s2))
    print(reverse_words_2(s))
    print(reverse_words_2(s1))
    print(reverse_words_2(s2))
