class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        counter = 0
        pre = None
        s = list(s)
        for item in s:
            if item != pre:
                counter += 1
            else:
                if max_len < counter:
                    max_len = counter
                counter = 0
            pre = item
        return max_len

if __name__ == '__main__':
    a = "abcabcbb"
    b = Solution()
    print(b.findJudge(3, a))