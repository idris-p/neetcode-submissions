class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31

        while n > 0:
            if n & 1 == 1:
                result += 2 ** power
            power -= 1
            n = n >> 1

        return result