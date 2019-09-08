import math

# 暴力枚举
# 执行结果：
# 通过
# 显示详情
# 执行用时 :
# 420 ms, 在所有 Python3 提交中击败了42.81%的用户
# 内存消耗 :
# 13.8 MB, 在所有 Python3 提交中击败了8.44%的用户
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         res = False
#         i = 0
#         while (i * i <= c):
#             num_sqr = c - i*i
#             num = math.sqrt(num_sqr)
#             if num % 1 == 0:
#                 res = True
#                 break
#             i += 1
#         return res

    
# 双指针
# 执行结果：
# 通过
# 显示详情
# 执行用时 :
# 284 ms, 在所有 Python3 提交中击败了66.77%的用户
# 内存消耗 :
# 13.7 MB, 在所有 Python3 提交中击败了8.44%的用户
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        res = False
        i = 0
        j = int(math.sqrt(c)) # j一定是c开平方最大的数
        
        while (i <= j):
            num = i * i + j * j
            if num == c:
                res = True
                break
                
            elif num > c:
                j -= 1
                
            else:
                i += 1
                
        return res
                

if __name__ == "__main__":
    solution = Solution()
    print(solution.judgeSquareSum(4))