#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        

        if n % 2 == 1:
            return self.myPow(x, n-1) * x
        else:
            return self.myPow(x*x, n/2)
