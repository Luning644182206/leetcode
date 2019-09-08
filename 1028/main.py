class Solution:
    def baseNeg2(self, N):
        bin_n = bin(N)
        bin_n_string = str(bin_n)[2:]

        bin_n_len = len(bin_n_string)
        res = 0
        for i in range(bin_n_len):
            if bin_n_string[i] == '1':
                res += pow(-2, bin_n_len-1)
            bin_n_len -= 1
        return res


if __name__ == '__main__':
    a = 2
    b = Solution()
    print(b.baseNeg2(a))