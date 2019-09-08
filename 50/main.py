class Solution:
    # 把问题变成分治算法
    # 复杂读为时间logn
    # n为奇数的时候 y=x*x^(n-1)
    # n为偶数的时候 y=x^(n/2)*x^(n/2)
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        
        # 小于0的情况
        if n < 0:
            return 1/self.myPow(x, -n)
        
        # 是奇数
        if n % 2:
            return x * self.myPow(x, n-1)
        
        #偶数
        return self.myPow(x*x, n/2)