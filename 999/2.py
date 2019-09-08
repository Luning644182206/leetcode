# coding=-utf8

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        counter = 0
        result = N
        num = N - 1
        result_arr = []
        first = True
        result_num = 0
        if result != 1:
            for i in range(N-1):
                print(result,counter, num)
                if counter is 0:
                    result *= num
                elif counter is 1:
                    result /= num
                elif counter is 2:
                    if first:
                        result += num
                        first = False
                    else:
                        result -= num
                # elif counter is 3:
                #     result -= num
                if counter is 2:
                    counter = 0
                    result_arr.append(int(result))
                    result = num - 1
                    num -= 1
                else:
                    counter += 1
                num -= 1
                result = int(result)
                if num <= 0:
                    result_arr.append(int(result))
                    break
            counter = 0
            for item in result_arr:
                if counter == 0:
                    result_num = item
                else:
                    result_num -= item
                counter += 1
            print(result_arr)
        else:
            result_num = 1
        return result_num



        # counter = 0
        # result = N
        # num = N - 1
        # for i in range(N-1):
        #     print(result,counter, num)
        #     if counter is 0:
        #         result *= num
        #     elif counter is 1:
        #         result /= num
        #     elif counter is 2:
        #         result += num
        #     elif counter is 3:
        #         result -= num
        #     if counter is 3:
        #         counter = 0
        #     else:
        #         counter += 1
        #     num -= 1
        #     result = int(result)
        # return result
           
if __name__ == '__main__':
    a = 16
    b = Solution()
    
    print(b.clumsy(a))

