class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualTotal = 0
        n = 0
        zeroPresent = False
        
        for num in nums:
            if num == 0:
                zeroPresent = True

            n = max(n, num)
            actualTotal += num

        if not zeroPresent:
            return 0

        expectedTotal = 0
        for i in range(n + 1):
            expectedTotal += i

        if expectedTotal - actualTotal == 0:
            return n + 1
            
        return expectedTotal - actualTotal