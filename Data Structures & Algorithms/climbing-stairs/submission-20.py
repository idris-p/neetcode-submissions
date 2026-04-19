class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1

        for i in range(0, n):
            if i + 1 <= n:
                table[i + 1] += table[i]
            if i + 2 <= n:
                table[i + 2] += table[i]

        return table[n]