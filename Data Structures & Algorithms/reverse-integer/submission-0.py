class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = x < 0

        numString = str(x)
        if negative:
            numString = numString[1:]

        for i, digit in enumerate(numString):
            result += int(digit) * 10 ** i

        if result > 2**31:
            return 0

        return result if not negative else -result