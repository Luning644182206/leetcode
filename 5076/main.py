# coding=utf-8
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if str1 == "" or str2 == "":
            return res
        if len(str1) % len(str2) == 0:
            num = len(str1) / len(str2) # 得到倍数
            str2_temp = int(num) * str2
            for i in range(len(str1)):

        return res
if __name__ == '__main__':
    str1 = "ABCABC"
    str2 = "ABC"
    a = Solution()
    a.gcdOfStrings(str1, str2)