# coding=utf-8

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_n_arr = list(bin(N))
        for index,item in enumerate(bin_n_arr[1:]):
            if item == '1':
                bin_n_arr[index+1] = '0'
            elif item == '0':
                bin_n_arr[index+1] = '1'
        # int_n_arr = int(bin(''.join(bin_n_arr)), 2)
        int_n_arr = int(''.join(bin_n_arr), 2)
        return int_n_arr


if __name__ == '__main__':
    a = 5
    b = Solution()
    
    print(b.bitwiseComplement(a))
    # a = [1,1,1,1,None]
    # print()