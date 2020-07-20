class Solution:
    def reverseWords(self, s):
        if s is None:
            return
        split_s = s.split(" ")
        print(split_s)
        st = ""
        for item in reversed(split_s):
            if item != '':
                st += item + " "
        return st


if __name__ == "__main__":
    s = "a good   example"
    ret = Solution().reverseWords(s)
    print(ret)