class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        l, r = 1, 2
        for i in range(2, n):
            l, r = r, l + r

        return r