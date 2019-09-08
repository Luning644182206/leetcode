# coding=-utf8

class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        # 找到abc，依次删除
        is_valid = False
        while S:
            if S.find('abc') >= 0:
                s_arr = S.split('abc')
                S = ''.join(s_arr)
            else:
                break
        if S == '':
            is_valid = True
        return is_valid
           
if __name__ == '__main__':
    a = 'cababc'
    b = Solution()
    
    print(b.isValid(a))

# def count():
#     fs = []
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             result = g()
#             return result
#         r = f(i)
#         fs.append(r)
#     return fs
# f1, f2, f3 = count()
# print(f1, f2, f3)


