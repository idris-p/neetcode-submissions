class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        x, y = 1, 1

        for i in range(1, n):
            temp = y
            y = x + y
            x = temp

        return y