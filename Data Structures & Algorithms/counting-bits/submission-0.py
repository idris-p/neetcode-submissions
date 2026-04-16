class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(0, n + 1):
            ones = 0
            current = i

            while current != 0:
                ones += current % 2
                current = current >> 1

            result[i] = ones

        return result