def is_palindrome(x):
    if x < 0 or x % 10 == 0 and x != 0:
        return False
    reverted_number = 0
    while x > reverted_number:
        reverted_number = reverted_number * 10 + x % 10
        print(reverted_number)
        x //= 10
        print(x)
    return x == reverted_number or x == reverted_number / 10


x = 12321
print(is_palindrome(x))
