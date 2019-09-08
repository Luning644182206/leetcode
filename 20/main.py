class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 大神版本
        s = list(s)
        s_arr = []
        s_hash = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        is_valid = True
        for item in s:
            if item not in s_hash.keys():
                s_arr.append(item)
            # important
            elif not s_arr or s_hash[item] != s_arr.pop():
                    is_valid = False
                    break
        
        return not s_arr


        # 菜鸡版本
        # s = list(s)
        # s_arr = []
        # is_valid = False
        # for item in s:
        #     if item == '{' or item == '(' or item == '[':
        #         s_arr.append(item)
        #     else:
        #         s_arr_len = len(s_arr)
        #         if s_arr_len > 0:
        #             if item == '}' and s_arr[-1] == '{':
        #                 s_arr.pop(-1)
        #             elif item == ']' and s_arr[-1] == '[':
        #                 s_arr.pop(-1)
        #             elif item == ')' and s_arr[-1] == '(':
        #                 s_arr.pop(-1)
        #             else:
        #                 s_arr.append(item)
        #                 break
        #         else:
        #             s_arr.append(item)
        #             break
        # if len(s_arr) == 0:
        #     is_valid = True
        # return is_valid



if __name__ == "__main__":
    a = ']'
    b = Solution()
    print(b.isValid(a))