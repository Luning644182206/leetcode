class Solution:
    
    def finder(self, N, x):
        if x > 0 and x < N:
            if N % x == 0:
                N = N - x
                return True, N
            else:
                x += 1
                return self.finder(N, x)
        else:
            return False, N
    
    
    def divisorGame(self, N: int) -> bool:
        # aleax = False
        # bob = False
        if N == 1:
            return False
        result = None
        while N > 1:
            aleax, N = self.finder(N, 1)
            bob, N = self.finder(N, 1)
            if aleax is True and bob is False:
                result = True
            else:
                result = False
        return result


if __name__ == '__main__':
    a = 2
    b = Solution()
    print(b.divisorGame(a))